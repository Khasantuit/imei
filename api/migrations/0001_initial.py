# Generated by Django 5.1.3 on 2025-02-11 13:09

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bolim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Boshqarma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClientData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(max_length=255)),
                ('father_name', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(max_length=13)),
                ('jshir', models.CharField(max_length=14)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Unvon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('father_name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(max_length=13, unique=True)),
                ('jton', models.CharField(max_length=8, unique=True)),
                ('lavozim', models.CharField(blank=True, max_length=100, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('bolim', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.bolim')),
                ('boshqarma', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.boshqarma')),
                ('unvon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.unvon')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ArizaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('imei', models.CharField(max_length=255)),
                ('last_simcard', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('info', models.TextField()),
                ('shakl1', models.CharField(max_length=30)),
                ('status', models.CharField(choices=[('yaratildi', 'Yaratildi'), ('qidiruvda', 'Qidiruvda'), ('topild', 'Topildi'), ('yopildi', 'Yakunlandi')], default='yaratildi', max_length=50)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.clientdata')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JinoyatIshiModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('jinoyat_raqami', models.CharField(max_length=255)),
                ('fish', models.CharField(max_length=255)),
                ('jshir', models.CharField(max_length=255)),
                ('info', models.TextField()),
                ('phone_number', models.CharField(max_length=13)),
                ('status', models.CharField(choices=[('ochilgan', 'Yangi'), ('qaytarilgan', 'Qaytarilgan'), ('sud', 'Sudga chiqarildi'), ('yopildi', 'Yopilgan')], default='yopilgan', max_length=50)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
