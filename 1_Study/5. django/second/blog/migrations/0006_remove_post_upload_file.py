# Generated by Django 3.1.2 on 2020-11-22 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20201122_1248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='upload_file',
        ),
    ]
