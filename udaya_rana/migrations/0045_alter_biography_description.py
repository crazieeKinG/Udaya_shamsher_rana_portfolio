# Generated by Django 3.2.11 on 2022-01-30 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udaya_rana', '0044_rename_achivements_counter_achievements_counter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biography',
            name='description',
            field=models.TextField(blank=True, default='No data found'),
        ),
    ]