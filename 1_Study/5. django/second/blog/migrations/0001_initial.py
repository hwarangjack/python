# Generated by Django 3.1.2 on 2020-11-19 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('who', models.CharField(max_length=30)),
                ('text', models.TextField()),
                ('picture', models.ImageField(upload_to='')),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
