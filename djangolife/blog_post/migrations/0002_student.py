# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-25 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('roll_no', models.TextField()),
                ('classs', models.TextField()),
            ],
        ),
    ]
