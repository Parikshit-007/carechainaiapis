# Generated by Django 4.1.13 on 2024-04-19 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hos_login', '0007_rename_user_custom_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='custom_user',
            name='last_login',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
