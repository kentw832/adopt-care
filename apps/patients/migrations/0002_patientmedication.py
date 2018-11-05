# Generated by Django 2.0.7 on 2018-08-09 20:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_employeeprofile_status'),
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientMedication',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('dose_mg', models.IntegerField()),
                ('date_prescribed', models.DateField()),
                ('duration_days', models.IntegerField()),
                ('refills', models.IntegerField(default=0)),
                ('instructions', models.CharField(blank=True, max_length=480, null=True)),
                ('medication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Medication')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.PatientProfile')),
                ('prescribing_practitioner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.EmployeeProfile')),
            ],
            options={
                'ordering': ('patient', 'medication'),
            },
        ),
    ]
