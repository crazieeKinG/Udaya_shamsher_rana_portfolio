# Generated by Django 3.2.11 on 2022-01-28 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udaya_rana', '0011_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio_data',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
