# Generated by Django 2.0.7 on 2019-05-03 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0056_auto_20190502_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vitaltask',
            name='vital_template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vital_tasks', to='tasks.CarePlanVitalTemplate'),
        ),
    ]
