# Generated by Django 2.0.7 on 2018-09-17 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_remove_patientmedication_refills'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientprofile',
            name='emr_code',
            field=models.CharField(blank=True, help_text="By adding the emr code to the patient profile, we can link patients to the electronic medical records (EMR). If the user is not in the emr they won't have an emr number.", max_length=100, null=True),
        ),
    ]
