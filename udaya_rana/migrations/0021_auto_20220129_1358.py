# Generated by Django 3.2.11 on 2022-01-29 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('udaya_rana', '0020_auto_20220129_1307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='user',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='user',
            new_name='author',
        ),
    ]
