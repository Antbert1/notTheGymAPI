# Generated by Django 3.2.6 on 2021-08-16 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('type', models.CharField(max_length=60)),
                ('tags', models.TextField(default='')),
                ('blurb', models.TextField(default='')),
            ],
        ),
    ]
