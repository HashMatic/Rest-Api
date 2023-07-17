from django.urls import path
from .views import ResumeAPIView

urlpatterns = [
    path('resume/', ResumeAPIView.as_view(), name='resume_api'),
]
