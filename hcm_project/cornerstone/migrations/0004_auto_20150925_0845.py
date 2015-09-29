# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cornerstone', '0003_auto_20150925_0836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cornerstoneuserprofile',
            name='manager_id',
        ),
        migrations.AddField(
            model_name='cornerstoneuserprofile',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', blank=True, to='cornerstone.CornerstoneUserProfile', null=True),
        ),
    ]
