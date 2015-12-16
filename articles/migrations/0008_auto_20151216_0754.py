# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import articles.models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_article_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.FileField(null=True, blank=True, upload_to=articles.models.get_upload_filename),
        ),
    ]
