# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-06 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='abstract',
            field=models.TextField(default=None, verbose_name='abstract'),
        ),
    ]