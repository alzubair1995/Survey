from flask import Flask
from pathlib import Path
from werkzeug.security import generate_password_hash

from extensions import db, login_manager

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "change-this-secret-key"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    base_dir = Path(__file__).resolve().parent
    db_dir = base_dir / "database"
    db_file = db_dir / "app.db"
    db_dir.mkdir(parents=True, exist_ok=True)

    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_file.as_posix()}"

    db.init_app(app)
    login_manager.init_app(app)

    # Blueprints
    from routes.main import main_bp
    from routes.auth import auth_bp
    from routes.admin import admin_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)

    @login_manager.user_loader
    def load_user(user_id):
        from models.user import User
        return User.query.get(int(user_id))

    with app.app_context():
        from models.user import User
        from models.response import SurveyResponse  # noqa: F401

        db.create_all()

        # Admin default
        admin_email = "ali@admin.com"
        admin = User.query.filter_by(email=admin_email).first()
        if not admin:   
            admin = User(
                name="Survey Admin",
                email=admin_email,
                password=generate_password_hash("Ali@123"),
                role="admin",
            )
            db.session.add(admin)
            db.session.commit()
            print("✅ DB ready + ADMIN created (ali@admin.com / Admin@123)")
        else:
            print("✅ DB ready + ADMIN already exists")

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
