# Generated by Django 3.2.11 on 2022-01-30 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udaya_rana', '0033_achivements_counter_slider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achivements_counter',
            name='icon',
            field=models.CharField(choices=[('bi bi-award-fill', '<i class="bi bi-award-fill"></i>'), ('bi bi-check-square-fill', '<i class="bi bi-check-square-fill"></i>'), ('bi bi-award-fill', '<i class="bi bi-award-fill"></i>'), ('bi bi-award-fill', '<i class="bi bi-award-fill"></i>'), ('bi bi-award-fill', '<i class="bi bi-award-fill"></i>')], default='award_fill', max_length=500),
        ),
    ]
