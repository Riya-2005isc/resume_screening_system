import os
import sys
import re

from flask import Flask, render_template, request

# Add project root to Python path
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)
sys.path.insert(0, PROJECT_ROOT)

from utils.resume_parser import (
    extract_text_from_pdf,
    preprocess_text
)

app = Flask(
    __name__,
    template_folder=os.path.join(PROJECT_ROOT, "templates")
)


# --------------------------------------------------
# HOME
# --------------------------------------------------

@app.route("/")
def home():
    return render_template("index.html")


# --------------------------------------------------
# SKILLS REQUIRED BY JOB DESCRIPTION
# --------------------------------------------------

STANDARD_SKILLS = [
    "python",
    "sql",
    "machine learning",
    "nlp",
    "pandas",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "power bi",
    "tableau",
    "docker",
    "aws",
    "git"
]


# --------------------------------------------------
# CERTIFICATIONS
# --------------------------------------------------

CERTIFICATIONS = [
    "aws",
    "google",
    "microsoft",
    "python",
    "tensorflow"
]


# --------------------------------------------------
# EXTRACT SKILLS
# --------------------------------------------------

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in STANDARD_SKILLS:

        if skill.lower() in text:
            found_skills.append(skill)

    return sorted(list(set(found_skills)))


# --------------------------------------------------
# EXTRACT EXPERIENCE
# --------------------------------------------------

def extract_experience(text):

    pattern = r'(\d+)\s*\+?\s*years?'

    match = re.search(pattern, text.lower())

    if match:
        return int(match.group(1))

    return 0


# --------------------------------------------------
# SKILL SCORE
# --------------------------------------------------

def calculate_skill_score(resume_text, job_skills):

    resume_text = resume_text.lower()

    matched_skills = []

    for skill in job_skills:

        if skill.lower() in resume_text:
            matched_skills.append(skill)

    if len(job_skills) == 0:
        score = 0
    else:
        score = (
            len(matched_skills) /
            len(job_skills)
        ) * 100

    missing_skills = [
        skill
        for skill in job_skills
        if skill not in matched_skills
    ]

    return round(score, 2), matched_skills, missing_skills


# --------------------------------------------------
# EXPERIENCE SCORE
# --------------------------------------------------

def calculate_experience_score(experience):

    try:
        experience = float(experience)
    except:
        return 0

    if experience >= 4:
        return 100

    elif experience >= 2:
        return 80

    elif experience >= 1:
        return 60

    else:
        return 40


# --------------------------------------------------
# EDUCATION SCORE
# --------------------------------------------------

def calculate_education_score(text):

    text = text.lower()

    if "master" in text or "m.tech" in text or "mtech" in text:
        return 100

    elif (
        "b.tech" in text
        or "btech" in text
        or "bachelor" in text
    ):
        return 80

    else:
        return 50


# --------------------------------------------------
# CERTIFICATION SCORE
# --------------------------------------------------

def calculate_certification_score(text):

    text = text.lower()

    matched = 0

    for certification in CERTIFICATIONS:

        if certification in text:
            matched += 1

    score = (
        matched /
        len(CERTIFICATIONS)
    ) * 100

    return round(score, 2)


# --------------------------------------------------
# FINAL CATEGORY
# --------------------------------------------------

def assign_category(score):

    if score >= 85:
        return "Excellent Match"

    elif score >= 70:
        return "Strong Match"

    elif score >= 55:
        return "Good Match"

    elif score >= 40:
        return "Average Match"

    else:
        return "Low Match"


# --------------------------------------------------
# UPLOAD + SCREENING
# --------------------------------------------------

@app.route("/upload", methods=["POST"])
def upload():

    jd = request.files.get("job_description")

    resumes = request.files.getlist("resumes")

    # Check JD
    if not jd:
        return {
            "error": "Please upload a Job Description."
        }, 400

    # Check resumes
    if not resumes:
        return {
            "error": "Please upload at least one resume."
        }, 400


    # --------------------------------------------------
    # EXTRACT JOB DESCRIPTION
    # --------------------------------------------------

    try:

        jd_raw_text = extract_text_from_pdf(jd)

        jd_text = preprocess_text(
            jd_raw_text
        )

    except Exception as e:

        return {
            "error": f"Could not process Job Description: {str(e)}"
        }, 500


    # --------------------------------------------------
    # FIND REQUIRED SKILLS FROM JD
    # --------------------------------------------------

    job_skills = extract_skills(jd_text)


    # --------------------------------------------------
    # PROCESS EACH RESUME
    # --------------------------------------------------

    candidates = []


    for resume in resumes:

        try:

            resume_raw_text = extract_text_from_pdf(
                resume
            )

            resume_text = preprocess_text(
                resume_raw_text
            )

        except Exception as e:

            candidates.append({
                "name": resume.filename,
                "error": str(e)
            })

            continue


        # ----------------------------------------------
        # SKILLS
        # ----------------------------------------------

        skill_score, matched_skills, missing_skills = (
            calculate_skill_score(
                resume_text,
                job_skills
            )
        )


        # ----------------------------------------------
        # EXPERIENCE
        # ----------------------------------------------

        experience = extract_experience(
            resume_raw_text
        )

        experience_score = calculate_experience_score(
            experience
        )


        # ----------------------------------------------
        # EDUCATION
        # ----------------------------------------------

        education_score = calculate_education_score(
            resume_raw_text
        )


        # ----------------------------------------------
        # CERTIFICATION
        # ----------------------------------------------

        certification_score = calculate_certification_score(
            resume_raw_text
        )


        # ----------------------------------------------
        # FINAL WEIGHTED SCORE
        # ----------------------------------------------

        final_score = (
            0.50 * skill_score
            + 0.25 * experience_score
            + 0.15 * education_score
            + 0.10 * certification_score
        )

        final_score = round(
            final_score,
            2
        )


        # ----------------------------------------------
        # CATEGORY
        # ----------------------------------------------

        category = assign_category(
            final_score
        )


        # ----------------------------------------------
        # STORE RESULT
        # ----------------------------------------------

        candidates.append({

            "name": resume.filename,

            "score": final_score,

            "category": category,

            "matched_skills": matched_skills,

            "missing_skills": missing_skills,

            "experience": experience,

            "experience_score": experience_score,

            "education_score": education_score,

            "certification_score": certification_score,

            "skill_score": skill_score,

            "resume_length": len(resume_text)

        })


    # --------------------------------------------------
    # SORT BY SCORE
    # --------------------------------------------------

    candidates.sort(
        key=lambda x: x.get("score", 0),
        reverse=True
    )


    # --------------------------------------------------
    # ADD RANK
    # --------------------------------------------------

    for rank, candidate in enumerate(
        candidates,
        start=1
    ):

        candidate["rank"] = rank


    # --------------------------------------------------
    # FINAL RESPONSE
    # --------------------------------------------------

    return {

        "job_description_length": len(jd_text),

        "required_skills": job_skills,

        "total_resumes": len(resumes),

        "candidates": candidates

    }
