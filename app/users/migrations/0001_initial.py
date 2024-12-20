# Generated by Django 5.1.3 on 2024-11-21 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.IntegerField(verbose_name='Айди пользователя в телеграм')),
                ('nickname', models.CharField(max_length=32, verbose_name='Никнейм пользователя')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
