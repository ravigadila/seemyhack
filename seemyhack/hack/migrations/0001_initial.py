# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-10 12:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('feedback_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('deletion_date', models.DateTimeField(null=True)),
                ('last_edit', models.DateTimeField(null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('-creation_date',),
                'verbose_name': 'Hack',
                'verbose_name_plural': 'Hacks',
            },
        ),
        migrations.CreateModel(
            name='HackFallower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fallow_time', models.DateTimeField(auto_now_add=True)),
                ('hack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hack.Hack')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('description', models.CharField(max_length=1000)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Topic',
                'verbose_name_plural': 'Topics',
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voted_datetime', models.DateTimeField(auto_now_add=True)),
                ('hack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hack.Hack')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-voted_datetime',),
                'verbose_name': 'Vote',
                'verbose_name_plural': 'Votes',
            },
        ),
        migrations.AddField(
            model_name='hack',
            name='topics',
            field=models.ManyToManyField(null=True, to='hack.Topic'),
        ),
        migrations.AddField(
            model_name='hack',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feedback',
            name='hack',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hack.Hack'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hack.Feedback'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
