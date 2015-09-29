# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cornerstone', '0005_auto_20150925_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cornerstoneuserprofile',
            name='manager_guid',
            field=models.UUIDField(blank=True),
        ),
        migrations.AlterField(
            model_name='cornerstoneuserprofile',
            name='user_id',
            field=models.UUIDField(unique=True),
        ),
    ]
