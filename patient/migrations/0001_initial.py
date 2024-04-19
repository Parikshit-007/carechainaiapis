# Generated by Django 3.2.9 on 2023-12-06 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('PatientID', models.AutoField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=255)),
                ('LastName', models.CharField(max_length=255)),
                ('DOB', models.DateField()),
                ('Gender', models.CharField(max_length=10)),
                ('ContactNumber', models.CharField(max_length=15)),
                ('Address', models.TextField()),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentInformation',
            fields=[
                ('TreatmentID', models.AutoField(primary_key=True, serialize=False)),
                ('TreatmentDetails', models.TextField()),
                ('PatientID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
        migrations.CreateModel(
            name='PatientVisitList',
            fields=[
                ('VisitID', models.AutoField(primary_key=True, serialize=False)),
                ('VisitDate', models.DateField()),
                ('Reason', models.TextField()),
                ('PatientID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
        migrations.CreateModel(
            name='PatientReminder',
            fields=[
                ('ReminderID', models.AutoField(primary_key=True, serialize=False)),
                ('ReminderDetails', models.TextField()),
                ('PatientID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
        migrations.CreateModel(
            name='PatientLedger',
            fields=[
                ('LedgerID', models.AutoField(primary_key=True, serialize=False)),
                ('TransactionDetails', models.TextField()),
                ('PatientID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
        migrations.CreateModel(
            name='PatientHistory',
            fields=[
                ('HistoryID', models.AutoField(primary_key=True, serialize=False)),
                ('MedicalHistoryDetails', models.TextField()),
                ('TreatmentDetails', models.TextField()),
                ('PatientID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
        migrations.CreateModel(
            name='PatientBilling',
            fields=[
                ('BillingID', models.AutoField(primary_key=True,default=False, serialize=False)),
                ('InvoiceDetails', models.TextField()),
                ('PatientID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
    ]
