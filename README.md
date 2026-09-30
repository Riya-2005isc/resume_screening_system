# 📄 Resume Screening System Using NLP

An NLP-based Resume Screening System that automatically analyzes resumes and compares them with a Job Description (JD). The system extracts candidate information, identifies skills, calculates similarity, and ranks candidates based on their suitability.

---

# 1. 📌 Project Overview

Recruiters often receive a large number of resumes for a single job position. Manually reviewing every resume is time-consuming.

This project uses Natural Language Processing (NLP) to automate the initial resume screening process.

The system processes 100 ATS-style PDF resumes and compares them with a Data Scientist Job Description.

---

# 2. 🎯 Objectives

- Extract text from PDF resumes
- Clean and normalize resume text
- Extract candidate information
- Identify technical skills and experience
- Apply NLP techniques
- Compare resumes with a Job Description
- Calculate candidate matching scores
- Identify matched and missing skills
- Rank candidates automatically

---

# 3. 📂 Dataset

The project uses:

- 100 ATS-style PDF resumes
- 1 Job Description

### Resume Information

- Name
- Email
- Phone Number
- Education
- Skills
- Work Experience
- Projects
- Certifications

### Job Role

**Data Scientist**

### Required Skills

- Python
- SQL
- Machine Learning
- NLP
- Pandas
- Scikit-learn
- TensorFlow
- Tableau

---

# 4. 🧠 NLP Techniques Used

## 4.1 Text Normalization

Resume text is cleaned and converted into a consistent format using lowercase conversion, removal of unnecessary characters, tokenization, stop-word removal, and lemmatization.

## 4.2 Regular Expressions

Regular Expressions are used to extract information such as email addresses, phone numbers, and experience from resumes.

## 4.3 Lemmatization

Lemmatization converts words into their base form.

Example:

```text
learning → learn
projects → project
skills → skill    
