# Generated by Django 3.2.11 on 2022-01-30 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udaya_rana', '0045_alter_biography_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mainmenu_background',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.FileField(upload_to='')),
                ('background', models.FileField(upload_to='')),
                ('achievement', models.FileField(upload_to='')),
                ('slider', models.FileField(upload_to='')),
                ('contact', models.FileField(upload_to='')),
            ],
        ),
    ]
