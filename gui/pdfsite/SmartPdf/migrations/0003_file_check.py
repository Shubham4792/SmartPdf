# Generated by Django 2.0.4 on 2018-11-04 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SmartPdf', '0002_auto_20181104_0126'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='check',
            field=models.BooleanField(default=False),
        ),
    ]