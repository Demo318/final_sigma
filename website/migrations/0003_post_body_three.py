# Generated by Django 4.0.6 on 2022-07-26 00:45

from django.db import migrations
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_post_body_two'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body_three',
            field=martor.models.MartorField(default='body number 3'),
            preserve_default=False,
        ),
    ]