# Generated by Django 2.0.6 on 2018-06-16 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180614_1058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='create_time',
            new_name='published_time',
        ),
    ]
