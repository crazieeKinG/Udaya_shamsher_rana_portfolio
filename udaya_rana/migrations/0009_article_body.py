# Generated by Django 3.2.11 on 2022-01-27 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udaya_rana', '0008_alter_video_video_category_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='body',
            field=models.TextField(default=' '),
        ),
    ]