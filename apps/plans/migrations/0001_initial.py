# Generated by Django 2.0.7 on 2018-07-23 15:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarePlanInstance',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.PatientProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CarePlanTemplate',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('type', models.CharField(choices=[('rpm', 'Remote Patient Management'), ('bhi', 'Behavioral Health Initiative'), ('cocm', 'Psychiatric Collaberative Care Management'), ('ccm', 'Chronic Care Management'), ('cccm', 'Complex Chronic Care Management'), ('tcm', 'Transitional Care Management')], max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=140)),
                ('description', models.CharField(max_length=240)),
                ('focus', models.CharField(max_length=140)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PlanConsent',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('verbal_consent', models.BooleanField(default=False)),
                ('discussed_co_pay', models.BooleanField(default=False)),
                ('seen_within_year', models.BooleanField(default=False)),
                ('will_use_mobile_app', models.BooleanField(default=False)),
                ('will_interact_with_team', models.BooleanField(default=False)),
                ('will_complete_tasks', models.BooleanField(default=False)),
                ('plan_instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plans.CarePlanInstance')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TeamTask',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=140)),
                ('category', models.CharField(max_length=120)),
                ('start_on_day', models.IntegerField()),
                ('frequency', models.CharField(choices=[('once', 'Once'), ('daily', 'Daily'), ('every_other_day', 'Every Other Day'), ('weekdays', 'Weekdays'), ('weekends', 'Weekends')], default='once', max_length=20)),
                ('repeat_amount', models.IntegerField(default=-1)),
                ('appear_time', models.TimeField()),
                ('due_time', models.TimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='careplantemplate',
            name='goals',
            field=models.ManyToManyField(blank=True, to='plans.Goal'),
        ),
        migrations.AddField(
            model_name='careplantemplate',
            name='team_tasks',
            field=models.ManyToManyField(blank=True, to='plans.TeamTask'),
        ),
        migrations.AddField(
            model_name='careplaninstance',
            name='plan_template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plans.CarePlanTemplate'),
        ),
    ]
