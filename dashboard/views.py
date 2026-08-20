from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from resume.models import Resume

@login_required
def dashboard(request):
    user_resumes = Resume.objects.filter(user=request.user)
    total_resumes = user_resumes.count()
    latest_resume = user_resumes.order_by("-uploaded_at").first()
    highest_score_obj = user_resumes.order_by("-resume_score").first()
    highest_score = highest_score_obj.resume_score if highest_score_obj else 0
    recent_resumes = user_resumes.order_by("-uploaded_at")[:4]

    context = {
        "total_resumes": total_resumes,
        "latest_resume": latest_resume,
        "highest_score": highest_score,
        "recent_resumes": recent_resumes,
    }
    return render(request, "dashboard/dashboard.html", context)
