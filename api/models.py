from django.db import models

class UserInfo(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_details = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resumes/')

