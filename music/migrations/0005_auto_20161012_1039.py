# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-12 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_album_is_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='audio_file',
            field=models.FileField(upload_to=b''),
        ),
    ]
