# Generated by Django 3.2.11 on 2022-01-29 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('udaya_rana', '0031_alter_bio_data_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bio_data',
            new_name='Biography',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
