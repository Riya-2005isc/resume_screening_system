import streamlit as st

st.set_page_config(page_title="Resume Screening System", page_icon="📄")

st.title("📄 Resume Screening System using NLP")

st.write("Welcome to the Resume Screening System.")

jd = st.file_uploader("Upload Job Description (PDF)", type=["pdf"])

resumes = st.file_uploader(
    "Upload Resume(s)",
    type=["pdf"],
    accept_multiple_files=True
)

if st.button("Screen Resumes"):
    st.success("Application is working! The NLP model will be connected next.")
