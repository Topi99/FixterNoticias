# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-02 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='noticia',
            options={'ordering': ('-fecha', '-categoria')},
        ),
        migrations.AddField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
