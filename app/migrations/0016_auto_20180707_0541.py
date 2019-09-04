# Generated by Django 2.0.6 on 2018-07-07 05:41

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20180704_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=20, verbose_name='the folder name')),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to='upload_image/', width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=app.models.upload_location, width_field='width_field'),
        ),
    ]