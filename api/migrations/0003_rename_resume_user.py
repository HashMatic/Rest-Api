# Generated by Django 4.2.3 on 2023-07-18 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_userinfo_resume'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Resume',
            new_name='User',
        ),
    ]
