# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import giza.models


class Migration(migrations.Migration):

    dependencies = [
        ('giza', '0002_auto_20170517_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giza',
            name='belongto',
            field=models.CharField(default=b'\xed\x95\x9c\xea\xb2\xa8\xeb\xa0\x88', max_length=b'20', choices=[(b'\xec\xa1\xb0\xec\x84\xa0\xec\x9d\xbc\xeb\xb3\xb4', b'\xec\xa1\xb0\xec\x84\xa0\xec\x9d\xbc\xeb\xb3\xb4'), (b'\xec\xa4\x91\xec\x95\x99\xec\x9d\xbc\xeb\xb3\xb4', b'\xec\xa4\x91\xec\x95\x99\xec\x9d\xbc\xeb\xb3\xb4'), (b'\xeb\x8f\x99\xec\x95\x84\xec\x9d\xbc\xeb\xb3\xb4', b'\xeb\x8f\x99\xec\x95\x84\xec\x9d\xbc\xeb\xb3\xb4'), (b'\xed\x95\x9c\xea\xb2\xa8\xeb\xa0\x88', b'\xed\x95\x9c\xea\xb2\xa8\xeb\xa0\x88'), (b'\xea\xb2\xbd\xed\x96\xa5\xec\x8b\xa0\xeb\xac\xb8', b'\xea\xb2\xbd\xed\x96\xa5\xec\x8b\xa0\xeb\xac\xb8'), (b'\xec\x98\xa4\xeb\xa7\x88\xec\x9d\xb4\xeb\x89\xb4\xec\x8a\xa4', b'\xec\x98\xa4\xeb\xa7\x88\xec\x9d\xb4\xeb\x89\xb4\xec\x8a\xa4'), (b'\xeb\xaf\xb8\xeb\x94\x94\xec\x96\xb4\xec\x98\xa4\xeb\x8a\x98', b'\xeb\xaf\xb8\xeb\x94\x94\xec\x96\xb4\xec\x98\xa4\xeb\x8a\x98'), (b'KBS', b'KBS'), (b'MBC', b'MBC'), (b'SBS', b'SBS'), (b'TV\xec\xa1\xb0\xec\x84\xa0', b'TV\xec\xa1\xb0\xec\x84\xa0'), (b'\xec\xb1\x84\xeb\x84\x90A', b'\xec\xb1\x84\xeb\x84\x90A'), (b'JTBC', b'JTBC'), (b'MBN', b'MBN'), (b'YTN', b'YTN'), (b'\xec\x97\xb0\xed\x95\xa9\xeb\x89\xb4\xec\x8a\xa4', b'\xec\x97\xb0\xed\x95\xa9\xeb\x89\xb4\xec\x8a\xa4'), (b'\xeb\x89\xb4\xec\x8b\x9c\xec\x8a\xa4', b'\xeb\x89\xb4\xec\x8b\x9c\xec\x8a\xa4'), (b'\xeb\x89\xb4\xec\x8a\xa41', b'\xeb\x89\xb4\xec\x8a\xa41'), (b'\xea\xb5\xad\xeb\xaf\xbc\xec\x9d\xbc\xeb\xb3\xb4', b'\xea\xb5\xad\xeb\xaf\xbc\xec\x9d\xbc\xeb\xb3\xb4'), (b'\xeb\x85\xb8\xec\xbb\xb7\xeb\x89\xb4\xec\x8a\xa4', b'\xeb\x85\xb8\xec\xbb\xb7\xeb\x89\xb4\xec\x8a\xa4'), (b'\xeb\x89\xb4\xeb\x8d\xb0\xec\x9d\xbc\xeb\xa6\xac', b'\xeb\x89\xb4\xeb\x8d\xb0\xec\x9d\xbc\xeb\xa6\xac'), (b'\xeb\x89\xb4\xec\x8a\xa4\xed\x83\x80\xed\x8c\x8c', b'\xeb\x89\xb4\xec\x8a\xa4\xed\x83\x80\xed\x8c\x8c'), (b'\xeb\x89\xb4\xec\x8a\xa4\xed\x86\xa0\xeb\xa7\x88\xed\x86\xa0', b'\xeb\x89\xb4\xec\x8a\xa4\xed\x86\xa0\xeb\xa7\x88\xed\x86\xa0'), (b'\xeb\x89\xb4\xec\x8a\xa4\xed\x95\x8c', b'\xeb\x89\xb4\xec\x8a\xa4\xed\x95\x8c'), (b'\xeb\x8d\xb0\xec\x9d\xbc\xeb\xa6\xac\xec\x95\x88', b'\xeb\x8d\xb0\xec\x9d\xbc\xeb\xa6\xac\xec\x95\x88'), (b'\xeb\xa7\xa4\xec\x9d\xbc\xea\xb2\xbd\xec\xa0\x9c', b'\xeb\xa7\xa4\xec\x9d\xbc\xea\xb2\xbd\xec\xa0\x9c'), (b'\xeb\xa8\xb8\xeb\x8b\x88\xed\x88\xac\xeb\x8d\xb0\xec\x9d\xb4', b'\xeb\xa8\xb8\xeb\x8b\x88\xed\x88\xac\xeb\x8d\xb0\xec\x9d\xb4'), (b'\xeb\xac\xb8\xed\x99\x94\xec\x9d\xbc\xeb\xb3\xb4', b'\xeb\xac\xb8\xed\x99\x94\xec\x9d\xbc\xeb\xb3\xb4'), (b'\xeb\xaf\xbc\xec\xa4\x91\xec\x9d\x98\xec\x86\x8c\xeb\xa6\xac', b'\xeb\xaf\xbc\xec\xa4\x91\xec\x9d\x98\xec\x86\x8c\xeb\xa6\xac'), (b'\xec\x84\x9c\xec\x9a\xb8\xec\x8b\xa0\xeb\xac\xb8', b'\xec\x84\x9c\xec\x9a\xb8\xec\x8b\xa0\xeb\xac\xb8'), (b'\xec\x84\xb8\xea\xb3\x84\xec\x9d\xbc\xeb\xb3\xb4', b'\xec\x84\xb8\xea\xb3\x84\xec\x9d\xbc\xeb\xb3\xb4'), (b'\xec\x8b\x9c\xec\x82\xaciN', b'\xec\x8b\x9c\xec\x82\xaciN'), (b'\xec\x8b\x9c\xec\x82\xac\xec\xa0\x80\xeb\x84\x90', b'\xec\x8b\x9c\xec\x82\xac\xec\xa0\x80\xeb\x84\x90'), (b'\xec\x9c\x84\xed\x82\xa4\xed\x8a\xb8\xeb\xa6\xac', b'\xec\x9c\x84\xed\x82\xa4\xed\x8a\xb8\xeb\xa6\xac'), (b'\xec\x9d\xb4\xeb\x8d\xb0\xec\x9d\xbc\xeb\xa6\xac', b'\xec\x9d\xb4\xeb\x8d\xb0\xec\x9d\xbc\xeb\xa6\xac'), (b'\xec\xbf\xa0\xed\x82\xa4\xeb\x89\xb4\xec\x8a\xa4', b'\xec\xbf\xa0\xed\x82\xa4\xeb\x89\xb4\xec\x8a\xa4'), (b'\xed\x94\x84\xeb\xa0\x88\xec\x8b\x9c\xec\x95\x88', b'\xed\x94\x84\xeb\xa0\x88\xec\x8b\x9c\xec\x95\x88'), (b'\xed\x95\x9c\xea\xb5\xad\xea\xb2\xbd\xec\xa0\x9c', b'\xed\x95\x9c\xea\xb5\xad\xea\xb2\xbd\xec\xa0\x9c'), (b'\xed\x95\x9c\xea\xb5\xad\xec\x9d\xbc\xeb\xb3\xb4', b'\xed\x95\x9c\xea\xb5\xad\xec\x9d\xbc\xeb\xb3\xb4')]),
        ),
        migrations.AlterField(
            model_name='giza',
            name='portrait',
            field=models.ImageField(blank=True, upload_to=b'portrait/', validators=[giza.models.validate_image]),
        ),
    ]
