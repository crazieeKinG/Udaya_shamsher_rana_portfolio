# Generated by Django 3.2.11 on 2022-01-30 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udaya_rana', '0047_mainmenu_background_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='video_category',
            name='status',
            field=models.CharField(choices=[('active', 'ACTIVE'), ('hide', 'HIDE')], default='active', max_length=500),
        ),
    ]
