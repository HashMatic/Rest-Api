from rest_framework import serializers
from .models import Resume

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ['user_name', 'email', 'contact_details', 'resume']

    def validate_resume(self, value):
        if not value.name.endswith('.pdf'):
            raise serializers.ValidationError("Resume must be in PDF format.")
        return value
