# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20151212_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
