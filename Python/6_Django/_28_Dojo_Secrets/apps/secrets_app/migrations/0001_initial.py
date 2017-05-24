# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-24 22:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Secrets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secret', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('authored_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authored_secrets', to='login_app.Users')),
                ('liked_by', models.ManyToManyField(related_name='likes_secrets', to='login_app.Users')),
            ],
        ),
    ]
