# Generated by Django 3.0.8 on 2020-07-04 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_songs_uploader'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songs',
            name='uploader',
        ),
    ]