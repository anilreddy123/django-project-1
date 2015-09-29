# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cornerstone', '0002_auto_20150925_0709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cornerstoneuserprofile',
            name='parent',
        ),
        migrations.AddField(
            model_name='cornerstoneuserprofile',
            name='manager_id',
            field=mptt.fields.TreeForeignKey(blank=True, to='cornerstone.CornerstoneUserProfile', null=True),
        ),
    ]
