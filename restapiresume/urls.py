from django.urls import path
from api.views import UserAPIView

urlpatterns = [
    path('api/user/', UserAPIView.as_view(), name='user_api'),
]


