# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-10-12 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_author_isactive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
    ]