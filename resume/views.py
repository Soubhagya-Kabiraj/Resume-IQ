from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .utils import extract_text_from_pdf, calculate_resume_score, find_skill_gap
from .forms import ResumeForm
from .models import Resume
from ml_engine.predictor import predict_role
from .recommendation import get_recommendations

def get_score_breakdown(text):
    text = (text or "").lower()
    skills = ["python", "django", "java", "javascript", "sql", "mysql", "html", "css", "bootstrap", "react", "machine learning", "git"]
    skill_count = sum(1 for s in skills if s in text)
    skill_score = min(skill_count * 3, 40)
    
    project_score = 20 if ("project" in text or "projects" in text) else 0
    
    edu_words = ["b.tech", "bachelor", "degree", "college", "university"]
    edu_score = 15 if any(w in text for w in edu_words) else 0
    
    exp_words = ["experience", "internship", "worked", "developer"]
    exp_score = 15 if any(w in text for w in exp_words) else 0
    
    cert_words = ["certificate", "certification", "course"]
    cert_score = 10 if any(w in text for w in cert_words) else 0
    
    return {
        "skills": skill_score,
        "projects": project_score,
        "education": edu_score,
        "experience": exp_score,
        "certifications": cert_score,
    }

@login_required
def upload_resume(request):
    if request.method == "POST":
        form = ResumeForm(
            request.POST,
            request.FILES
        )
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            text = extract_text_from_pdf(resume.resume_file.path)
            resume.extracted_text = text
            prediction = predict_role(text)
            resume.predicted_role = prediction["role"]
            resume.confidence = prediction["confidence"]
            resume.resume_score = calculate_resume_score(text)

            missing = find_skill_gap(
                text,
                prediction["role"]
            )
            resume.missing_skills = ", ".join(missing)

            recommended = get_recommendations(prediction["role"])
            resume.recommended_jobs = ", ".join(recommended)

            resume.save()
            messages.success(request, "Resume analyzed successfully!")
            return redirect("resume_detail", pk=resume.pk)
    else:
        form = ResumeForm()
    return render(request, "resume/upload_resume.html", {"form": form})

@login_required
def resume_history(request):
    resumes = Resume.objects.filter(
        user=request.user
    ).order_by("-uploaded_at")

    context = {"resumes": resumes}
    return render(request, "resume/resume_history.html", context)

@login_required
def resume_detail(request, pk):
    resume = get_object_or_404(
        Resume,
        pk=pk,
        user=request.user
    )
    missing_skills = []
    if resume.missing_skills:
        missing_skills = resume.missing_skills.split(", ")

    recommended_jobs = []
    if resume.recommended_jobs:
        recommended_jobs = resume.recommended_jobs.split(", ")

    score_breakdown = get_score_breakdown(resume.extracted_text)

    return render(
        request,
        "resume/resume_detail.html",
        {
            "resume": resume,
            "missing_skills": missing_skills,
            "recommended_jobs": recommended_jobs,
            "score_breakdown": score_breakdown
        }
    )

@login_required
def delete_resume(request, pk):
    resume = get_object_or_404(Resume, pk=pk, user=request.user)
    if request.method == "POST":
        resume.delete()
        messages.success(request, "Resume report deleted successfully.")
        return redirect("resume_history")
    return redirect("resume_detail", pk=pk)