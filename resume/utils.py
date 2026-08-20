import pdfplumber
from .skill_data import ROLE_SKILLS

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def calculate_resume_score_breakdown(text):
    text = (text or "").lower()
    
    # 1. Skills section (max 40 marks)
    skills = [
        "python", "django", "java", "javascript", "sql", "mysql", 
        "html", "css", "bootstrap", "react", "machine learning", "git",
        "c++", "c#", "php", "node", "aws", "docker"
    ]
    skill_count = sum(1 for skill in skills if skill in text)
    skill_score = min(skill_count * 3, 40)

    # 2. Projects section (max 20 marks)
    project_keywords = ["project", "projects", "key projects", "academic project"]
    project_score = 20 if any(word in text for word in project_keywords) else 0

    # 3. Education section (max 15 marks)
    education_keywords = ["b.tech", "bachelor", "degree", "college", "university", "master", "m.tech", "bca", "mca", "diploma", "education"]
    edu_score = 15 if any(word in text for word in education_keywords) else 0

    # 4. Experience section (max 15 marks)
    # Require explicit experience indicators (avoid generic terms like 'developer' or 'worked')
    experience_keywords = ["work experience", "professional experience", "internship", "intern"]
    exp_score = 15 if any(word in text for word in experience_keywords) else 0

    # 5. Certifications section (max 10 marks)
    certificate_keywords = ["certificate", "certification", "course", "certified"]
    cert_score = 10 if any(word in text for word in certificate_keywords) else 0

    total_score = min(skill_score + project_score + edu_score + exp_score + cert_score, 100)

    breakdown = {
        "skills": skill_score,
        "projects": project_score,
        "education": edu_score,
        "experience": exp_score,
        "certifications": cert_score,
        "total": total_score
    }
    return breakdown, total_score

def calculate_resume_score(text):
    _, total_score = calculate_resume_score_breakdown(text)
    return total_score

def find_skill_gap(resume_text, predicted_role):
    resume_text = (resume_text or "").lower()

    # Get required skills for predicted role
    required_skills = ROLE_SKILLS.get(predicted_role, [])
    missing_skills = []

    for skill in required_skills:
        if skill.lower() not in resume_text:
            missing_skills.append(skill)

    return missing_skills