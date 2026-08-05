from utils.resume_parser import extract_text_from_pdf, preprocess_text
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():

    jd = request.files["job_description"]
    resumes = request.files.getlist("resumes")

    jd_text = preprocess_text(extract_text_from_pdf(jd))

    output = []

    for resume in resumes:
        resume_text = preprocess_text(extract_text_from_pdf(resume))

        output.append({
            "name": resume.filename,
            "length": len(resume_text)
        })

    return {
        "Job Description Length": len(jd_text),
        "Resumes": output
    }
