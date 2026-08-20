from django.urls import path
from . import views

urlpatterns = [
    path("upload/", views.upload_resume, name="upload_resume"),
    path("history/", views.resume_history, name="resume_history"),
    path("<int:pk>/", views.resume_detail, name="resume_detail"),
    path("delete/<int:pk>/", views.delete_resume, name="delete_resume"),
]