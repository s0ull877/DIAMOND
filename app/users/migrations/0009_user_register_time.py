# Generated by Django 5.1.3 on 2024-12-01 16:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='register_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата регистрации'),
            preserve_default=False,
        ),
    ]
