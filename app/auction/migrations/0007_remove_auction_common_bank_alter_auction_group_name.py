# Generated by Django 5.1.3 on 2024-11-23 13:48

import shortuuid.main
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0006_remove_auction_bet_time_alter_auction_group_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='common_bank',
        ),
        migrations.AlterField(
            model_name='auction',
            name='group_name',
            field=models.CharField(blank=True, default=shortuuid.main.ShortUUID.uuid, editable=False, max_length=64, unique=True, verbose_name='Имя для группы ws'),
        ),
    ]
