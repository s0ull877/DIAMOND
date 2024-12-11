# Generated by Django 5.1.3 on 2024-12-04 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_user_dark_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='users_images/avatar.jpg', upload_to='users_images', verbose_name='аватар пользователя'),
        ),
    ]
