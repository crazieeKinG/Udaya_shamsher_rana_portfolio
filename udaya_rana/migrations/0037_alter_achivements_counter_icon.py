# Generated by Django 3.2.11 on 2022-01-30 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udaya_rana', '0036_alter_achivements_counter_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achivements_counter',
            name='icon',
            field=models.CharField(choices=[('<i class="bi bi-award-fill"></i>', '<i class="bi bi-award-fill"></i>'), ('bi bi-check-square-fill', '<i class="bi bi-check-square-fill"></i>'), ('bi bi-award-fill', '<i class="bi bi-award-fill"></i>'), ('bi bi-award-fill', '<i class="bi bi-award-fill"></i>'), ('bi bi-award-fill', '<i class="bi bi-award-fill"></i>'), ('bi bi-award-fill', '&#xf042;')], default='award_fill', max_length=500),
        ),
    ]
