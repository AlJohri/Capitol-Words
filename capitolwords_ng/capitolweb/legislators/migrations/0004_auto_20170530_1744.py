# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legislators', '0003_auto_20170529_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='type',
            field=models.CharField(choices=[('sen', 'Senate'), ('rep', 'House')], max_length=3),
        ),
    ]