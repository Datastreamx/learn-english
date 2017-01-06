# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-05 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0004_auto_20161130_0017'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilledOpenQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('question', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MultipleChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=2)),
                ('option_1', models.CharField(max_length=100)),
                ('option_2', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OpenQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=2)),
                ('question', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
            ],
        ),
    ]