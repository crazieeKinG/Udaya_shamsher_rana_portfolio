# Generated by Django 3.2.11 on 2022-01-28 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udaya_rana', '0016_auto_20220128_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='bio_data',
            name='image',
            field=models.CharField(default='None', max_length=1000),
        ),
    ]
