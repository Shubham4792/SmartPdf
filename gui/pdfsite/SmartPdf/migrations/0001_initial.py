# Generated by Django 2.0.4 on 2018-11-03 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('pages', models.CharField(max_length=4)),
            ],
            options={
                'db_table': 'file',
            },
        ),
    ]
