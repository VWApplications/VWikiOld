# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.CharField(default='fa fa-folder-open', help_text='Icones do Font Awesome', max_length=100, verbose_name='Icone'),
        ),
    ]
