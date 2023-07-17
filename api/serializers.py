from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.core import validators

class ResumeSerializer(serializers.Serializer):
    user_name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    contact_details = serializers.CharField(max_length=100)
    resume = serializers.FileField(allow_empty_file=False, validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'])])

    def validate_resume(self, value):
        if not value.name.endswith('.pdf'):
            raise ValidationError("File must be in PDF format.")
        return value
