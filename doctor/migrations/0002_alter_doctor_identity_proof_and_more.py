# Generated by Django 4.1.13 on 2024-02-01 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='identity_proof',
            field=models.FileField(upload_to='identity_proofs/'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='medical_liscence',
            field=models.FileField(upload_to='medical_licenses/'),
        ),
    ]
