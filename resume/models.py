from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    resume_file = models.FileField(
        upload_to="resumes/"
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    extracted_text = models.TextField(
        blank=True
    )

    predicted_role = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    confidence = models.FloatField(
        default=0,
        blank=True,
        null=True
    )

    resume_score = models.IntegerField(
        default=0
    )

    missing_skills = models.TextField(
        blank=True,
        null=True
    )

    recommended_jobs = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.uploaded_at.date()}"