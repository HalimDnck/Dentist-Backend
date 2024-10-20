# Generated by Django 5.1 on 2024-10-17 21:04

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('slug', models.CharField(max_length=256, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('deleted_on', models.DateTimeField(default=None, null=True)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('key', models.CharField(max_length=128, unique=True)),
                ('description', models.CharField(blank=True, max_length=600, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('slug', models.CharField(max_length=256, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('deleted_on', models.DateTimeField(default=None, null=True)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('key', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InsuranceProvider',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('slug', models.CharField(max_length=256, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('deleted_on', models.DateTimeField(default=None, null=True)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('key', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReferralSource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('slug', models.CharField(max_length=256, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('deleted_on', models.DateTimeField(default=None, null=True)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('key', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
