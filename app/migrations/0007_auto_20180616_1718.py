# Generated by Django 2.0.6 on 2018-06-16 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20180616_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='img3',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='file3'),
        ),
        migrations.AlterField(
            model_name='article',
            name='part2',
            field=models.TextField(blank=True, null=True, verbose_name='part2'),
        ),
        migrations.AlterField(
            model_name='article',
            name='part3',
            field=models.TextField(blank=True, null=True, verbose_name='part3'),
        ),
    ]
