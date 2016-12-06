# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-29 18:47
from __future__ import unicode_literals

from django.db import migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterField(
            model_name='post',
            name='conteudo',
            field=redactor.fields.RedactorField(verbose_name='Conteúdo'),
        ),
    ]