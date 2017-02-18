# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 22:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_remove_lesson_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='subtopic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='courses.Subtopic', verbose_name='Subtopico'),
            preserve_default=False,
        ),
    ]
