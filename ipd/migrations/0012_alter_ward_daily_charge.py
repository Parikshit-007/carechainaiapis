# Generated by Django 4.1.13 on 2024-07-02 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipd', '0011_alter_dischargehistory_discharge_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ward',
            name='daily_charge',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
