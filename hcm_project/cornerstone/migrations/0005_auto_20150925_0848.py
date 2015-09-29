# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cornerstone', '0004_auto_20150925_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cornerstoneuserprofile',
            name='guid',
            field=models.UUIDField(unique=True),
        ),
    ]
