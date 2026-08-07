import os
import sys

from flask import Flask, render_template, request

# Add project root to Python path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from utils.resume_parser import extract_text_from_pdf, preprocess_text

# Templates are in the root/templates folder
app = Flask(
    __name__,
    template_folder=os.path.join(PROJECT_ROOT, "templates")
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    jd = request.files.get("job_description")
    resumes = request.files.getlist("resumes")

    if not jd:
        return {"error": "Please upload a Job Description."}, 400

    if not resumes:
        return {"error": "Please upload at least one resume."}, 400

    jd_text = preprocess_text(
        extract_text_from_pdf(jd)
    )

    output = []

    for resume in resumes:

        resume_text = preprocess_text(
            extract_text_from_pdf(resume)
        )

        output.append({
            "name": resume.filename,
            "length": len(resume_text)
        })

    return {
        "Job Description Length": len(jd_text),
        "Resumes": output
    }
