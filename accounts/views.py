from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from resume.models import Resume

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()
        messages.success(request, "Account created successfully. Please sign in.")
        return redirect("login")
    return render(request, "accounts/register.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid credentials. Please try again.")
    return render(request, "accounts/login.html")

def logout_user(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("home")

@login_required
def profile(request):
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "update_info":
            first_name = request.POST.get("first_name", "")
            last_name = request.POST.get("last_name", "")
            email = request.POST.get("email", "")
            request.user.first_name = first_name
            request.user.last_name = last_name
            request.user.email = email
            request.user.save()
            messages.success(request, "Profile details updated successfully!")
            return redirect("profile")
        elif action == "change_password":
            current_pass = request.POST.get("current_password")
            new_pass = request.POST.get("new_password")
            confirm_pass = request.POST.get("confirm_password")
            if not request.user.check_password(current_pass):
                messages.error(request, "Current password is incorrect.")
            elif new_pass != confirm_pass:
                messages.error(request, "New passwords do not match.")
            elif len(new_pass) < 6:
                messages.error(request, "Password must be at least 6 characters long.")
            else:
                request.user.set_password(new_pass)
                request.user.save()
                login(request, request.user)  # Keep logged in
                messages.success(request, "Password changed successfully!")
            return redirect("profile")

    user_resumes = Resume.objects.filter(user=request.user)
    total_resumes = user_resumes.count()
    highest_score = user_resumes.order_by("-resume_score").first()
    latest_resume = user_resumes.order_by("-uploaded_at").first()

    context = {
        "total_resumes": total_resumes,
        "highest_score": highest_score.resume_score if highest_score else 0,
        "latest_resume": latest_resume,
    }
    return render(request, "accounts/profile.html", context)
