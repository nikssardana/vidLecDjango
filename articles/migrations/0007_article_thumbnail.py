# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import articles.models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20151212_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumbnail',
            field=models.FileField(default=None, upload_to=articles.models.get_upload_filename),
            preserve_default=False,
        ),
    ]
