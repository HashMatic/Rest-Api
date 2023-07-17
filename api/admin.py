from django.contrib import admin
from api.models import UserInfo

@admin.register(UserInfo)
class UserInfoModelAdmin(admin.ModelAdmin):
    list_display=['user_name', 'email', 'contact_details', 'resume']

