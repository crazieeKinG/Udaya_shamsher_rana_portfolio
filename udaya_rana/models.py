from ensurepip import bootstrap
from django.db import models
from datetime import datetime
from django.template.defaultfilters import truncatechars
from django.conf import settings
from django.utils.html import format_html
from django.utils.safestring import mark_safe

status_choices = (('active','ACTIVE'),('hide', 'HIDE'))

# Create your models here.
class Mainmenu_background(models.Model):
    logo = models.FileField()
    background = models.FileField()
    achievement = models.FileField()
    slider = models.FileField()
    contact = models.FileField()
    status = models.CharField(max_length=500, choices=status_choices, default='active')

    def logo_image(self):        
        return format_html('<img src="{}" style="max-height: 150px"/>', self.logo.url)
    logo_image.short_description = 'Logo Image'
    logo_image.allow_tags = True

    def background_image(self):        
        return format_html('<img src="{}" style="max-height: 150px"/>', self.background.url)
    background_image.short_description = 'Background Image'
    background_image.allow_tags = True

    def achievement_image(self):        
        return format_html('<img src="{}" style="max-height: 150px"/>', self.achievement.url)
    achievement_image.short_description = 'Achievement Image'
    achievement_image.allow_tags = True

    def slider_image(self):        
        return format_html('<img src="{}" style="max-height: 150px"/>', self.slider.url)
    slider_image.short_description = 'Slider Image'
    slider_image.allow_tags = True

    def contact_image(self):        
        return format_html('<img src="{}" style="max-height: 150px"/>', self.contact.url)
    contact_image.short_description = 'Contact Image'
    contact_image.allow_tags = True

class Slider(models.Model):
    caption = models.CharField(max_length=1000)
    image = models.FileField(verbose_name='Slider image')
    created = models.DateTimeField(default=datetime.now, blank=True)
    status = models.CharField(max_length=500, choices=status_choices, default='active')

    def image_tag(self):        
        return format_html('<img src="{}" style="max-height: 150px"/>', self.image.url)
    image_tag.short_description = 'Slider Image'
    image_tag.allow_tags = True

class Achievements_counter(models.Model):
    title = models.CharField(max_length=1000)
    count = models.IntegerField(verbose_name="Number of achievements")
    image = models.FileField()
    created = models.DateTimeField(default=datetime.now, blank=True)
    status = models.CharField(max_length=500, choices=status_choices, default='active')

    def image_tag(self):        
        return format_html('<img src="{}" style="max-height: 150px"/>', self.image.url)
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

class Album(models.Model):
    cover_image = models.FileField(max_length=1000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    description = models.TextField()
    created = models.DateTimeField(default=datetime.now, blank=True)
    status = models.CharField(max_length=500, choices=status_choices, default='active')

    def image_tag(self):        
        return format_html('<img src="{}" style="max-height: 150px"/>', self.cover_image.url)
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __str__(self):
        return self.name

class Image(models.Model):
    album = models.ForeignKey(Album, default=0, on_delete=models.CASCADE)
    file = models.FileField(max_length=1000)
    caption = models.CharField(max_length=1000)
    created = models.DateTimeField(default=datetime.now, blank=True)
    status = models.CharField(max_length=500, choices=status_choices, default='active')
    records = 0

    def image_tag(self):        
        return format_html('<img src="{}" style="max-height: 150px"/>', self.file.url)
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

class Contact_us(models.Model):
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    contact_number = models.CharField(max_length=500)
    message = models.TextField()
    created = models.DateTimeField(default=datetime.now, blank=True)


class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    body = models.TextField(default=" ")
    image = models.FileField(max_length=1000)
    event_date = models.DateField(default=datetime.now, blank=True)
    status = models.CharField(max_length=500, choices=status_choices, default='active')
    created = models.DateTimeField(default=datetime.now, blank=True)

    def body_truncate(self):
       return truncatechars(self.body, 500)
    body_truncate.short_description = 'Description'
    body_truncate.allow_tags = True

    
    def image_tag(self):        
        return format_html('<img src="{}" style="max-height: 150px"/>', self.image.url)
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    
class Mainmenu(models.Model):
    label = models.CharField(max_length=1000)
    reference = models.CharField(max_length=1000)
    order_by = models.IntegerField(default=99)

class Video_category(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    created = models.DateTimeField(default=datetime.now, blank=True)
    cover_image = models.FileField(max_length=1000)
    status = models.CharField(max_length=500, choices=status_choices, default='active')

    def __str__(self):
        return self.title

    def image_tag(self):        
        return format_html('<img src="{}" style="max-height: 150px"/>', self.cover_image.url)
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

class Video(models.Model):
    video_category = models.ForeignKey(Video_category, default=0, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000, verbose_name="Link [Embeded link only]")
    status = models.CharField(max_length=500, choices=status_choices, default='active')
    created = models.DateTimeField(default=datetime.now, blank=True)

class Biography(models.Model):
    name = models.CharField(max_length=1000)
    dob = models.DateField(blank=True, verbose_name="Date of birth")
    address = models.CharField(max_length=1000)
    description = models.TextField(default="No data found",blank=True)
    image = models.FileField(max_length=1000, verbose_name="Profile picture")
    telephone = None
    email = None
    titles = None
    records = 0

    def __str__(self):
        return self.name

    def body_truncate(self):
       return truncatechars(self.description, 200)
    body_truncate.short_description = 'Description'
    body_truncate.allow_tags = True

    def image_tag(self):        
        return format_html('<img src="{}" style="max-height: 150px"/>', self.image.url)
    image_tag.short_description = 'Profile picture'
    image_tag.allow_tags = True

class Telephone(models.Model):
    bio_data = models.ForeignKey(Biography, default=0, on_delete=models.CASCADE)
    number = models.CharField(max_length=1000)

    def __str__(self):
        return self.bio_data.name

class Email(models.Model):
    bio_data = models.ForeignKey(Biography, default=0, on_delete=models.CASCADE)
    email = models.CharField(max_length=1000)

    def __str__(self):
        return self.bio_data.name

class Title(models.Model):
    bio_data = models.ForeignKey(Biography, default=0, on_delete=models.CASCADE)
    role = models.CharField(max_length=1000)
        
    def __str__(self):
        return self.bio_data.name


class Education(models.Model):
    bio_data = models.ForeignKey(Biography, default=0, on_delete=models.CASCADE)
    institute_name = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    acadamic_level = models.CharField(max_length=1000)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.bio_data.name


class Political_background(models.Model):
    bio_data = models.ForeignKey(Biography, default=0, on_delete=models.CASCADE)
    description = models.TextField()    

    def __str__(self):
        return self.bio_data.name


class Work_experience(models.Model):
    bio_data = models.ForeignKey(Biography, default=0, on_delete=models.CASCADE)
    institute_name = models.CharField(max_length=1000)
    role = models.TextField()
    description = models.TextField(blank=True)    

    def __str__(self):
        return self.bio_data.name

class Activity(models.Model):
    bio_data = models.ForeignKey(Biography, default=0, on_delete=models.CASCADE)
    institute_name = models.CharField(max_length=1000)
    role = models.TextField()
    description = models.TextField(blank=True)    

    def __str__(self):
        return self.bio_data.name

class Travel(models.Model):
    bio_data = models.ForeignKey(Biography, default=0, on_delete=models.CASCADE)
    description = models.TextField()    

    def __str__(self):
        return self.bio_data.name

class International_program(models.Model):
    bio_data = models.ForeignKey(Biography, default=0, on_delete=models.CASCADE)
    description = models.TextField()    

    def __str__(self):
        return self.bio_data.name

class Publication(models.Model):
    bio_data = models.ForeignKey(Biography, default=0, on_delete=models.CASCADE)
    description = models.TextField()    

    def __str__(self):
        return self.bio_data.name

class Skill(models.Model):
    bio_data = models.ForeignKey(Biography, default=0, on_delete=models.CASCADE)
    description = models.TextField()    

    def __str__(self):
        return self.bio_data.name
    