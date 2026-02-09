from flask import Blueprint, render_template, request, redirect, url_for, flash
from extensions import db
from models.response import SurveyResponse

main_bp = Blueprint("main", __name__)

@main_bp.route("/", methods=["GET", "POST"])
def survey():
    if request.method == "POST":
        payload = SurveyResponse(
            gender=request.form.get("gender"),
            education_stage=request.form.get("education_stage"),
            satisfaction=request.form.get("satisfaction"),
            understanding_help=request.form.get("understanding_help"),
            device=request.form.get("device"),
            internet_quality=request.form.get("internet_quality"),
            platform_ease=request.form.get("platform_ease"),
            teacher_interaction=request.form.get("teacher_interaction"),
            study_preference=request.form.get("study_preference"),
            continue_elearning=request.form.get("continue_elearning"),
        )

        db.session.add(payload)
        db.session.commit()
        return render_template("survey.html", success=True)

    return render_template("survey.html", success=False)

@main_bp.route("/about")
def about():
    return render_template("about.html")
