# Generated by Django 5.1.3 on 2024-12-02 17:41

import shortuuid.main
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tictactoes', '0006_alter_tictactoe_group_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tictactoe',
            name='group_name',
            field=models.CharField(blank=True, default=shortuuid.main.ShortUUID.uuid, editable=False, max_length=64, unique=True, verbose_name='Имя для группы ws'),
        ),
    ]
