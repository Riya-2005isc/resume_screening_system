# 📄 Resume Screening System Using NLP

An NLP-based Resume Screening System that automatically analyzes resumes and compares them with a Job Description (JD). It helps identify suitable candidates by extracting skills, calculating similarity, and ranking resumes.

## 🎯 1. Project Objectives

- Analyze resumes automatically
- Extract candidate information
- Identify skills and experience
- Compare resumes with a Job Description
- Calculate matching scores
- Identify matched and missing skills
- Rank candidates

## 📂 2. Dataset

The project uses:

- **100 ATS-style PDF resumes**
- **1 Data Scientist Job Description**

### Required Skills

- Python
- SQL
- Machine Learning
- NLP
- Pandas
- Scikit-learn
- TensorFlow
- Tableau

## 🧠 3. NLP Techniques Used

### 3.1 Text Normalization
Cleans and standardizes resume text.

### 3.2 Regular Expressions
Extracts email, phone number, and other candidate information.

### 3.3 Lemmatization
Converts words into their base form.

Example:
learning → learn
projects → project
skills → skill

### 3.4 POS Tagging
Identifies nouns, verbs, adjectives, and other word types.

### 3.5 TF-IDF
Converts resume and JD text into numerical vectors.

### 3.6 Cosine Similarity
Measures similarity between the resume and JD.

### 3.7 Edit Distance
Identifies spelling variations.
Example:
pythn → python

## 4. Methodology
100 PDF Resumes
       ↓
PDF Text Extraction
       ↓
Text Cleaning
       ↓
Information Extraction
       ↓
Skill & Experience Extraction
       ↓
Lemmatization
       ↓
POS Tagging
       ↓
TF-IDF
       ↓
Cosine Similarity
       ↓
Spelling Correction
       ↓
Skill Matching
       ↓
Candidate Scoring
       ↓
Candidate Ranking

## 🛠️ 5. Technologies Used
Python
Pandas
NumPy
spaCy
NLTK
Scikit-learn
PDFPlumber
Regular Expressions
TF-IDF
Cosine Similarity
Edit Distance
Vercel

## 🌐 6. Deployment

The Resume Screening System is deployed using Vercel.

🔗 Live Demo

https://resume-screening-system-xfz4.vercel.app/

## 📈 7. Results

The system automatically analyzes 100 resumes, compares them with the Data Scientist Job Description, identifies matched and missing skills, calculates scores, and ranks candidates.

## 👩‍💻 8. Author

Riya Rathod

NLP Case Study Project

This is the version I’d use for your **GitHub README** because it is detailed enough to explain the case study but still short and clean.
