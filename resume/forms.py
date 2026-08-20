from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ["resume_file"]
        widgets = {
            "resume_file": forms.FileInput(attrs={
                "class": "hidden-file-input",
                "accept": ".pdf",
                "id": "pdf-file-input"
            })
        }