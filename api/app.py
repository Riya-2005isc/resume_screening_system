import streamlit as st
import pdfplumber
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Resume Screening System", layout="wide")

st.title("📄 Resume Screening System using NLP")

# -------------------------
# Function to extract text
# -------------------------
def extract_text(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

# -------------------------
# Text preprocessing
# -------------------------
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9 ]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text

# -------------------------
# Upload files
# -------------------------
jd_file = st.file_uploader(
    "Upload Job Description (PDF)",
    type=["pdf"]
)

resume_files = st.file_uploader(
    "Upload Resume PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

# -------------------------
# Screen resumes
# -------------------------
if st.button("Screen Resumes"):

    if jd_file is None:
        st.error("Please upload a Job Description.")
        st.stop()

    if len(resume_files) == 0:
        st.error("Please upload at least one Resume.")
        st.stop()

    jd_text = preprocess(extract_text(jd_file))

    resume_names = []
    resume_texts = []

    for resume in resume_files:
        resume_names.append(resume.name)
        resume_texts.append(preprocess(extract_text(resume)))

    documents = [jd_text] + resume_texts

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    result = pd.DataFrame({
        "Resume": resume_names,
        "ATS Score (%)": (similarity * 100).round(2)
    })

    result = result.sort_values(
        by="ATS Score (%)",
        ascending=False
    )

    st.success("Screening Completed")

    st.dataframe(result, use_container_width=True)

    st.bar_chart(result.set_index("Resume"))
