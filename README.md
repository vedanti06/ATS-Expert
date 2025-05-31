# ATS Resume Expert 🧠📄

An AI-powered Applicant Tracking System (ATS) Resume Analyzer built with **Streamlit** and **Gemini (Google Generative AI)**.

This tool helps job seekers evaluate how well their resume matches a specific job description. It provides feedback like:
- Resume summary analysis
- ATS match percentage
- Missing keywords and suggestions

---

## 🔧 Features

- Upload resume in **PDF** format
- Input custom **job descriptions**
- Receive feedback from **Gemini Pro Vision API**
- Outputs:
  - Strengths & weaknesses
  - Percentage match
  - Missing keywords & suggestions

---
## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/vedanti06/ats-resume-expert.git
cd ats-resume-expert

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt

Create a .env file and add your Gemini API key:
GOOGLE_API_KEY=your_google_generative_ai_key_here

streamlit run app.py

