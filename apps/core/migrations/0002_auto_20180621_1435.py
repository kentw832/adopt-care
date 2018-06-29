# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-06-21 20:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='facility',
            options={'verbose_name_plural': 'facilities'},
        ),
        migrations.AddField(
            model_name='providertitle',
            name='abbreviation',
            field=models.CharField(default=None, max_length=10),
            preserve_default=False,
        ),
    ]