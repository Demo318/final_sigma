# Generated by Django 4.0.6 on 2022-07-26 01:15

from django.db import migrations
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body_three',
            field=martor.models.MartorField(default='New post spot.'),
            preserve_default=False,
        ),
    ]