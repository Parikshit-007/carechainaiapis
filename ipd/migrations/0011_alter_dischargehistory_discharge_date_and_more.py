# Generated by Django 4.1.13 on 2024-06-17 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipd', '0010_alter_dischargehistory_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dischargehistory',
            name='discharge_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ipddischarge',
            name='discharge_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ipdregistration',
            name='discharge_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]