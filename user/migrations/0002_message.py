# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-31 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fromUserId', models.CharField(max_length=200)),
                ('toUserId', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=2000)),
            ],
        ),
    ]
