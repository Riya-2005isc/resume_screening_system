from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    jd = request.files.get("job_description")
    resumes = request.files.getlist("resumes")

    if not jd:
        return "Please upload a Job Description."

    if len(resumes) == 0:
        return "Please upload at least one resume."

    return f"""
    <h2>Files Uploaded Successfully!</h2>
    <p>Job Description: {jd.filename}</p>
    <p>Number of Resumes: {len(resumes)}</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
