# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-19 13:32
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('mobile', models.CharField(blank=True, max_length=11, null=True, verbose_name='手机号')),
                ('image', models.ImageField(default='image/default.png', upload_to='image/%Y/%m', verbose_name='头像')),
                ('name', models.CharField(default='', max_length=32, verbose_name='姓名')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'userprofile',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='HostPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updatedatetime', models.DateTimeField(auto_created=True, auto_now=True, verbose_name='更新时间')),
                ('createdatetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('groups', models.ManyToManyField(to='asset.HostGroup', verbose_name='主机组')),
            ],
            options={
                'verbose_name': '权限',
                'verbose_name_plural': '权限',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='菜单')),
                ('icon', models.CharField(blank=True, max_length=32, null=True, verbose_name='图标')),
            ],
            options={
                'verbose_name': '菜单组',
                'verbose_name_plural': '菜单组',
                'db_table': 'rbac_menu',
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='菜单名')),
                ('url', models.CharField(max_length=256, verbose_name='菜单url')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='URL别名')),
                ('menu', models.ForeignKey(blank=True, help_text='null表示非菜单;非null表示是二级菜单', null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Menu', verbose_name='所属菜单')),
                ('pid', models.ForeignKey(blank=True, help_text='对于无法作为菜单的URL，可以为其选择一个可以作为菜单的权限，那么访问时，则默认选中此权限', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parents', to='users.Permission', verbose_name='关联的权限')),
            ],
            options={
                'verbose_name': '菜单',
                'verbose_name_plural': '菜单',
                'db_table': 'rbac_permission',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='角色名')),
                ('permissions', models.ManyToManyField(blank=True, to='users.Permission', verbose_name='拥有的所有权限')),
            ],
            options={
                'verbose_name': '用户角色',
                'verbose_name_plural': '用户角色',
                'db_table': 'rbac_role',
            },
        ),
        migrations.CreateModel(
            name='WxConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agentid', models.CharField(max_length=50, verbose_name='授权方网页应用ID')),
                ('redirect_uri', models.CharField(max_length=255, verbose_name='重定向地址')),
                ('state', models.CharField(max_length=255, verbose_name='状态')),
                ('corpid', models.CharField(max_length=128, verbose_name='CorpID')),
                ('corp_secret', models.CharField(max_length=128, verbose_name='Secret')),
            ],
            options={
                'verbose_name': '企业微信配置',
                'verbose_name_plural': '企业微信配置',
                'db_table': 'wxconfig',
            },
        ),
        migrations.AddField(
            model_name='hostpermission',
            name='permissions',
            field=models.ManyToManyField(related_name='permission', to='auth.Permission', verbose_name='权限'),
        ),
        migrations.AddField(
            model_name='hostpermission',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='permissionuser', to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='roles',
            field=models.ManyToManyField(to='users.Role', verbose_name='拥有的角色'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
