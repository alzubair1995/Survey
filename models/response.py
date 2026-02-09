from datetime import datetime
from extensions import db

class SurveyResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    student_name = db.Column(db.String(160), nullable=False)

    gender = db.Column(db.String(30), nullable=False)
    education_stage = db.Column(db.String(50), nullable=False)

    satisfaction = db.Column(db.String(50), nullable=False)
    understanding_help = db.Column(db.String(50), nullable=False)

    device = db.Column(db.String(50), nullable=False)
    internet_quality = db.Column(db.String(50), nullable=False)

    platform_ease = db.Column(db.String(50), nullable=False)
    teacher_interaction = db.Column(db.String(50), nullable=False)

    study_preference = db.Column(db.String(50), nullable=False)
    continue_elearning = db.Column(db.String(50), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
