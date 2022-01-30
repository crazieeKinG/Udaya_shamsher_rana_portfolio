# Generated by Django 3.2.11 on 2022-01-27 12:29

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('udaya_rana', '0002_auto_20220127_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('message', models.TextField()),
                ('created', models.DateField(blank=True, default=datetime.datetime.now)),
                ('contact_number', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('description', models.TextField()),
                ('start_date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('end_date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('status', models.CharField(max_length=1000)),
                ('cover_image', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Mainmenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=1000)),
                ('reference', models.CharField(max_length=1000)),
                ('order_by', models.IntegerField(default=99)),
                ('parent_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameField(
            model_name='album',
            old_name='cover_image_id',
            new_name='cover_image',
        ),
        migrations.RemoveField(
            model_name='image',
            name='user',
        ),
        migrations.AlterField(
            model_name='album',
            name='description',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='Video_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('created', models.DateField(blank=True, default=datetime.datetime.now)),
                ('updated', models.DateField(blank=True, default=datetime.datetime.now)),
                ('cover_image', models.CharField(max_length=1000)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('link', models.CharField(max_length=1000)),
                ('active', models.IntegerField(default=1)),
                ('created', models.DateField(blank=True, default=datetime.datetime.now)),
                ('updated', models.DateField(blank=True, default=datetime.datetime.now)),
                ('featured', models.BooleanField(default=False)),
                ('video_category_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='udaya_rana.album')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('image', models.CharField(max_length=1000)),
                ('event_date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('status', models.CharField(max_length=500)),
                ('created', models.DateField(blank=True, default=datetime.datetime.now)),
                ('updated', models.DateField(blank=True, default=datetime.datetime.now)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
