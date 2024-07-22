# Generated by Django 4.1.13 on 2024-07-21 08:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patient', '0001_initial'),
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OPD_REGISTER',
            fields=[
                ('visit_id', models.AutoField(primary_key=True, serialize=False)),
                ('visit_date', models.DateField(auto_now_add=True)),
                ('department', models.CharField(max_length=20)),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
                ('owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
        migrations.CreateModel(
            name='RefDoctorReport',
            fields=[
                ('report_id', models.AutoField(primary_key=True, serialize=False)),
                ('ref_doc_id', models.TextField()),
                ('referrals_details', models.TextField()),
                ('owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OPDTOIPDTRANSFER',
            fields=[
                ('transfer_id', models.AutoField(primary_key=True, serialize=False)),
                ('ipd_admission_id', models.TextField()),
                ('admission_date', models.DateField()),
                ('owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('visit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opd.opd_register')),
            ],
        ),
        migrations.CreateModel(
            name='OPDPatientSummary',
            fields=[
                ('summary_id', models.AutoField(primary_key=True, serialize=False)),
                ('summary_details', models.TextField(blank=True)),
                ('owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
        migrations.CreateModel(
            name='OPD_REPORT',
            fields=[
                ('report_id', models.AutoField(primary_key=True, serialize=False)),
                ('report_details', models.TextField(blank=True)),
                ('owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('visit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opd.opd_register')),
            ],
        ),
        migrations.CreateModel(
            name='OPD_PRESCRIPTION',
            fields=[
                ('prescription_id', models.AutoField(primary_key=True, serialize=False)),
                ('prescription_details', models.TextField(blank=True)),
                ('owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('visit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opd.opd_register')),
            ],
        ),
        migrations.CreateModel(
            name='OPD_Billing',
            fields=[
                ('billing_id', models.AutoField(primary_key=True, serialize=False)),
                ('invoice_detail', models.TextField(default=None)),
                ('owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('visit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opd.opd_register')),
            ],
        ),
        migrations.CreateModel(
            name='Depwisereport',
            fields=[
                ('report_id', models.AutoField(primary_key=True, serialize=False)),
                ('department', models.TextField()),
                ('date_details', models.DateField(default=None)),
                ('owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ConsultantDoctorReport',
            fields=[
                ('report_id', models.AutoField(primary_key=True, serialize=False)),
                ('consultant_doctor_id', models.TextField()),
                ('performance_details', models.TextField()),
                ('owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
