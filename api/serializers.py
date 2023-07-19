from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user_name', 'email', 'contact_details', 'resume']

    def validate_resume(self, resume):
        # Check if the uploaded file is a PDF
        if not resume.name.lower().endswith('.pdf'):
            raise serializers.ValidationError("Resume must be in PDF format.")
        return resume