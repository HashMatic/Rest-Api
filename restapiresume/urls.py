from django.urls import path
from api.views import UserProfileListAPIView, UserProfileDetailAPIView

urlpatterns = [
    path('profiles/', UserProfileListAPIView.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', UserProfileDetailAPIView.as_view(), name='profile-detail'),
]
