from django.urls import path
from .views import views

urlpatterns = [
    path('resumes/',views.resume_list),
]
