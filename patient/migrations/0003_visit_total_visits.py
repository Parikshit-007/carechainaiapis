# Generated by Django 4.1.13 on 2024-07-21 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_visit'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='total_visits',
            field=models.IntegerField(default=0),
        ),
    ]
