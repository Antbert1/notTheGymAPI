# Generated by Django 3.2.6 on 2021-08-16 15:01

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notgymapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classdetail',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, null=True, srid=4326),
        ),
    ]