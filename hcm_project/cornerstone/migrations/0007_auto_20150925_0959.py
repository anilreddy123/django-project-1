# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cornerstone', '0006_auto_20150925_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cornerstoneuserprofile',
            name='manager_guid',
            field=models.UUIDField(),
        ),
        migrations.AlterField(
            model_name='cornerstoneuserprofile',
            name='user_id',
            field=models.IntegerField(unique=True),
        ),
    ]
