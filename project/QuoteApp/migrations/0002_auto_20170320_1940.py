# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-03-20 14:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QuoteApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quotes',
            options={'verbose_name': 'Quote', 'verbose_name_plural': 'Quotes'},
        ),
        migrations.AlterField(
            model_name='quotes',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
