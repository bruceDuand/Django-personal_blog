# Generated by Django 2.0.6 on 2018-06-14 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180609_1534'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='title')),
                ('content', models.TextField(verbose_name='content')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='create time')),
                ('last_modified_time', models.DateTimeField(auto_now=True, verbose_name='last modified time')),
                ('status', models.CharField(choices=[('u', 'unfinished'), ('p', 'published')], max_length=1, verbose_name='status')),
                ('views', models.PositiveIntegerField(verbose_name='views time')),
                ('put_on_top', models.BooleanField(verbose_name='top')),
                ('abstract', models.CharField(blank=True, help_text='null is enabled', max_length=20, verbose_name='abstract')),
            ],
            options={
                'ordering': ['-last_modified_time'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Category name')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create time')),
                ('last_modified_time', models.DateTimeField(auto_now=True, verbose_name='Last modeified time')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Category'),
        ),
    ]
