# Generated by Django 4.0.6 on 2022-07-25 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_post_date_created_post_date_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_img',
            field=models.ImageField(default='header_imgs/default-post-header.jpeg', upload_to='header_imgs/'),
            preserve_default=False,
        ),
    ]