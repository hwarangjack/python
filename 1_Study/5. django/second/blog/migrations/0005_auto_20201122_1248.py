# Generated by Django 3.1.2 on 2020-11-22 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201120_1507'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='picture',
            new_name='upload_file',
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
