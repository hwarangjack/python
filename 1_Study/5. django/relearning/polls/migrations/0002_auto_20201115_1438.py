# Generated by Django 3.1.2 on 2020-11-15 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateTimeField(verbose_name='when you register this question'),
        ),
    ]