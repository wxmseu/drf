# Generated by Django 4.1.2 on 2022-10-24 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, unique=True, verbose_name='用户名')),
                ('user_type', models.SmallIntegerField(choices=[(1, '管理员'), (2, '普通用户'), (3, 'vip用户'), (4, '游客')], verbose_name='用户类型')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
                ('group', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.usergroup')),
                ('role', models.ManyToManyField(to='api.role')),
            ],
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=128, verbose_name='token')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.userinfo', verbose_name='用户名')),
            ],
        ),
    ]