# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-14 06:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PDFDeal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drawings',
            name='Size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='PDFDeal.DrawingSize', verbose_name='\u56fe\u5e45'),
        ),
    ]
