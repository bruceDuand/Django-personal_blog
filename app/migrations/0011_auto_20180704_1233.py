# Generated by Django 2.0.6 on 2018-07-04 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_delete_userfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='img1',
        ),
        migrations.RemoveField(
            model_name='article',
            name='img2',
        ),
        migrations.RemoveField(
            model_name='article',
            name='img3',
        ),
        migrations.RemoveField(
            model_name='article',
            name='part1',
        ),
        migrations.RemoveField(
            model_name='article',
            name='part2',
        ),
        migrations.RemoveField(
            model_name='article',
            name='part3',
        ),
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(null=True, verbose_name='content'),
        ),
    ]
