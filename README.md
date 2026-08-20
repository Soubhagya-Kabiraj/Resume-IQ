<div align="center">
<img width="100%" alt="ResumeIQ Home Page" src="https://github.com/user-attachments/assets/70be5158-14ef-4d82-9cc2-57e20d36ac28" />

---
  
  # ⚡ ResumeIQ 
  ### Next-Gen AI Resume Screening & Career Intelligence Platform

  [![Django](https://img.shields.io/badge/Django-5.0+-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
  [![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
  [![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
  [![License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)

  <p align="center">
    ResumeIQ is an executive-grade AI SaaS application designed to streamline talent acquisition and empower job seekers. It leverages Natural Language Processing (NLP) and Machine Learning (ML) to analyze PDF resumes, predict matching job roles, compute accurate ATS compatibility scores, and highlight skill gaps.
  </p>

</div>

---

## 🚀 Key Features

### 🤖 AI Job Role Classifier
- **TF-IDF & Naive Bayes Pipeline**: Scans extracted resume text to classify candidates into industry job profiles with model confidence metrics.
- **NLP Text Parser**: Fast, local PDF parsing powered by `pdfplumber` ensuring zero data leakage.

### 🎯 ATS Score & Parameter Breakdown
- **Weighted Scoring Engine**: Calculates an objective ATS compatibility score (0–100) evaluated across 5 key dimensions:
  - 💻 **Technical Skills** (Up to 40 pts)
  - 🚀 **Projects Section** (Up to 20 pts)
  - 🎓 **Education Criteria** (Up to 15 pts)
  - 💼 **Work & Internship Experience** (Up to 15 pts)
  - 📜 **Certifications** (Up to 10 pts)
- **Visual Gauges**: Color-coded score indicators (High / Moderate / Needs Improvement).

### 🔍 Skill Gap Profiling & Career Recommendations
- **Skill Deficiency Detector**: Compares candidate skills against job profile standards to generate targeted missing skill chips.
- **Career Role Matcher**: Suggests alternative job roles aligned with candidate strengths.

### 💻 Executive SaaS Dark UI System
- **Glassmorphism Aesthetic**: Dark slate theme (`#090d16`) with ambient glow meshes, responsive cards, and micro-interactions.
- **Interactive Drag & Drop Upload**: Custom file upload dropzone with live parsing animation scanner overlay.
- **Real-Time History Search**: Searchable resume archive with live client-side filtering.
- **Account Overview Portal**: User profile editor, activity stats, and password security tools.

---

## 📸 User Interface Preview
| 🏠 Home Page | 📊 Dashboard |
| --- | --- |
| <img width="100%" alt="ResumeIQ Home Page" src="https://github.com/user-attachments/assets/70be5158-14ef-4d82-9cc2-57e20d36ac28" /> | <img width="100%" alt="ResumeIQ Dashboard" src="https://github.com/user-attachments/assets/9c116d06-fba6-4fb1-a400-0fbafe8cb842" /> |

| 📊 Dashboard — Analytics | 🗂️ Resume History |
| --- | --- |
| <img width="100%" alt="ResumeIQ Dashboard Analytics" src="https://github.com/user-attachments/assets/a0449b9f-9306-428b-b1cf-f2484cfb36a7" /> | <img width="100%" alt="Resume History" src="https://github.com/user-attachments/assets/cf9bc00c-e4a0-4712-82d2-318d3426c07c" /> |

| 📄 Resume Details | 📄 Resume Details — Analysis |
| --- | --- |
| <img width="100%" alt="Resume Details" src="https://github.com/user-attachments/assets/ae72c341-6150-4182-a94a-d3266d58ba3e" /> | <img width="100%" alt="Resume Details Remaining" src="https://github.com/user-attachments/assets/5b931728-b328-4c57-a438-502a8d0c3ba0" /> |

| 🔍 PDF Text Extraction | 👤 User Profile Management |
| --- | --- |
| <img width="100%" alt="PDF Text Extraction" src="https://github.com/user-attachments/assets/c94d0f72-6857-4689-af0a-6dab0a9afe7f" /> | <img width="100%" alt="User Profile Management" src="https://github.com/user-attachments/assets/65a79d58-29e2-41e2-8c89-7b28a4b8143b" /> |

---

## 🛠️ Technology Stack

| Domain | Technology |
| :--- | :--- |
| **Backend Framework** | [Django 5](https://www.djangoproject.com/) |
| **Programming Language** | [Python 3.10+](https://www.python.org/) |
| **Machine Learning** | [Scikit-Learn](https://scikit-learn.org/), [Joblib](https://joblib.readthedocs.io/) |
| **PDF Extraction** | [pdfplumber](https://github.com/jsvine/pdfplumber) |
| **Frontend Layout** | HTML5, Vanilla CSS3 (Custom Design Tokens), Bootstrap 5 |
| **Icons & Typography** | Bootstrap Icons, Google Fonts (*Plus Jakarta Sans* & *Inter*) |
| **Database** | SQLite3 / PostgreSQL compatible |

---

## 📁 Project Architecture

```text
Resume_IQ/
├── ResumeIQ/              # Django Project Core Configuration (settings, urls, wsgi)
├── accounts/              # Authentication & User Profile Management App
├── core/                  # Landing Page & Public Pages App
├── dashboard/             # Main User Workspace Dashboard App
├── dataset/               # Training Datasets & Preprocessed Datasets
├── ml_engine/             # Machine Learning Model, TF-IDF Vectorizer & Training Scripts
├── resume/                # Core Parsing, Scoring & Resume Storage App
├── static/                # Global Static Assets
│   └── css/
│       └── style.css      # Custom Glassmorphic SaaS Design System
├── templates/             # HTML Templates System
│   ├── accounts/          # Login, Register, Profile templates
│   ├── core/              # Home landing template
│   ├── dashboard/         # Dashboard template
│   └── resume/            # Upload, Detail Report, and History templates
├── db.sqlite3             # Database Instance
├── manage.py              # Django CLI Runner
└── requirements.txt       # Project Dependencies
```

---

## ⚙️ Installation & Setup

Follow these steps to run **ResumeIQ** locally on your environment:

### 1. Prerequisites
- Python 3.10 or higher installed.
- Git installed.

### 2. Clone the Repository
```bash
git clone https://github.com/Soubhagya-Kabiraj/Resume-IQ.git
cd Resume-IQ
```

### 3. Create & Activate Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```
> *Note: Required packages include `django`, `scikit-learn`, `joblib`, `pdfplumber`, etc.*

### 5. Apply Database Migrations
```bash
python manage.py migrate
```

### 6. Start Development Server
```bash
python manage.py runserver
```

Open your browser and navigate to **`http://127.0.0.1:8000/`**.

---

## 📖 Usage Guide

1. **Account Registration**: Sign up for a free account or log in with existing credentials.
2. **Upload Resume**: Navigate to **Analyze Resume**, drag & drop a PDF resume into the scanner box, and click **Analyze Resume with AI**.
3. **Review AI Analytics Report**:
   - Inspect predicted job role and confidence score.
   - Analyze ATS score gauge and component breakdown.
   - Review missing skill gaps and recommended jobs.
   - View or copy extracted raw text from the built-in terminal inspector.
4. **Manage History**: Browse, search, or delete past resume reports under the **History** tab.
5. **Update Profile**: Manage your email or password in **Account Overview**.

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve ResumeIQ:

1. Fork the Project.
2. Create a Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git checkout origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## 📝 License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for more details.

---

<div align="center">
  <sub>Built with ❤️ by <a href="https://github.com/Soubhagya-Kabiraj">Soubhagya Kabiraj</a></sub>
</div>
