# Generated by Django 3.1.2 on 2020-11-20 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
