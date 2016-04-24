# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kursy', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kurs',
            options={'verbose_name_plural': 'Kursy'},
        ),
    ]
