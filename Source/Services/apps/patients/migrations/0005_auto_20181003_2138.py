# Generated by Django 2.0.7 on 2018-10-04 03:38

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_patientprofile_emr_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientVerificationCode',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=6)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verification_codes', to='patients.PatientProfile')),
            ],
            options={
                'verbose_name': 'Patient Verification Code',
                'verbose_name_plural': 'Patient Verification Codes',
            },
        ),
        migrations.AlterUniqueTogether(
            name='patientverificationcode',
            unique_together={('patient', 'code')},
        ),
    ]
