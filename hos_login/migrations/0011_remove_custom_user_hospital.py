# Generated by Django 4.1.13 on 2024-04-19 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hos_login', '0010_custom_user_is_active_custom_user_is_staff_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custom_user',
            name='hospital',
        ),
    ]
