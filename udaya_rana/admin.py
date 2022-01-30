from dataclasses import fields
from multiprocessing.dummy import active_children
from django.contrib import admin
from importlib_metadata import files
from .models import *
from django.forms import TextInput, Textarea

admin.site.site_header = "Admin Panel: Dashboard"

form_field = {
        models.CharField: {'widget': TextInput(attrs={'size':'150'})},
        models.TextField: {'widget': Textarea(attrs={'rows':25, 'cols': 150})},
    }

form_field_2 = {
        models.CharField: {'widget': TextInput(attrs={'size':'150'})},
        models.TextField: {'widget': Textarea(attrs={'rows':10, 'cols': 150})},
    }
# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
    formfield_overrides = form_field

    fields = ('author', 'name', 'description', 'status', 'cover_image', 'image_tag', 'created')
    readonly_fields = ('image_tag','created')
    list_display = ('name', 'author', 'description', 'status', 'image_tag', 'created')
    list_filter = ('status', 'author')

    list_per_page = 10
    

class ImageAdmin(admin.ModelAdmin):
    formfield_overrides = form_field

    fields = ('album', 'caption', 'status', 'file', 'image_tag', 'created')
    readonly_fields = ('created', 'image_tag')
    list_display = ('caption', 'album', 'status', 'image_tag', 'created')
    list_filter = ('status', 'album')

    list_per_page = 10

class ContactAdmin(admin.ModelAdmin):
    formfield_overrides = form_field

    fields = ('name', 'email', 'contact_number', 'message', 'created')
    readonly_fields = ('name', 'email', 'contact_number', 'message', 'created')
    list_display = ('name', 'email', 'contact_number', 'message', 'created')

    list_per_page = 10

class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = form_field

    fields = ('author', 'title', 'event_date', 'status', 'body', 'image', 'image_tag', 'created')
    readonly_fields = ('image_tag', 'created')
    list_display = ('title', 'author', 'event_date', 'status', 'image_tag',  'body_truncate', 'created')
    list_filter = ('status', 'event_date', 'author')

    list_per_page = 10

class MainMenuAdmin(admin.ModelAdmin):
    formfield_overrides = form_field

    fields = ('label', 'reference', 'order_by')
    list_display = ('label', 'reference', 'order_by')

    list_per_page = 10

class VideoCategoryAdmin(admin.ModelAdmin):
    formfield_overrides = form_field

    fields = ('author', 'title','cover_image', 'image_tag', 'status', 'created')
    readonly_fields = ('created', 'image_tag')
    list_display = ('title', 'author', 'cover_image', 'image_tag', 'status', 'created')
    list_filter = ('status', 'author')

    list_per_page = 10

class VideoAdmin(admin.ModelAdmin):
    formfield_overrides = form_field

    fields = ('video_category', 'title', 'link', 'status', 'created')
    readonly_fields = ('created',)
    list_display = ('title', 'video_category', 'link', 'status', 'created')
    list_filter = ('status', 'video_category')

    list_per_page = 10


class TelephoneAdmin(admin.TabularInline):
    formfield_overrides = form_field

    model = Telephone
    extra = 1

class EmailAdmin(admin.TabularInline):
    formfield_overrides = form_field

    model = Email
    extra = 1

class TitleAdmin(admin.TabularInline):
    formfield_overrides = form_field

    model = Title
    extra = 1

class EducationAdmin(admin.StackedInline):
    formfield_overrides = form_field_2

    model = Education
    extra = 1

class PoliticalBackgroundAdmin(admin.TabularInline):
    formfield_overrides = form_field_2

    model = Political_background
    extra = 1

class WorkExperienceAdmin(admin.StackedInline):
    formfield_overrides = form_field_2

    model = Work_experience
    extra = 1

class ActivityAdmin(admin.StackedInline):
    formfield_overrides = form_field_2

    model = Activity
    extra = 1

class TravelAdmin(admin.TabularInline):
    formfield_overrides = form_field_2

    model = Travel
    extra = 1

class InternationalProgramAdmin(admin.TabularInline):
    formfield_overrides = form_field_2

    model = International_program
    extra = 1

class PublicationAdmin(admin.TabularInline):
    formfield_overrides = form_field_2

    model = Publication
    extra = 1

class SkillAdmin(admin.TabularInline):
    formfield_overrides = form_field_2

    model = Skill
    extra = 1

class BioDataAdmin(admin.ModelAdmin):
    formfield_overrides = form_field

    inlines = [TelephoneAdmin, EmailAdmin, TitleAdmin, EducationAdmin, PoliticalBackgroundAdmin, WorkExperienceAdmin, ActivityAdmin, TravelAdmin, InternationalProgramAdmin, PublicationAdmin, SkillAdmin]

    fields = ('name', 'dob', 'address', 'description', 'image', 'image_tag')
    readonly_fields = ('image_tag',)
    list_display = ('name', 'dob', 'address', 'image_tag', 'body_truncate', 'telephone', 'email', 'title', 'education', 'political_background', 'work_experience', 'activity', 'travel', 'international_program', 'publication' ,'skill')
    
    list_per_page = 1

    def telephone(self, obj):
        return [s.number for s in Telephone.objects.filter(bio_data=obj).order_by('-id')[:2]]

    def email(self, obj):
        return [s.email for s in Email.objects.filter(bio_data=obj).order_by('-id')[:2]]

    def title(self, obj):
        return [s.role for s in Title.objects.filter(bio_data=obj).order_by('-id')[:2]]

    def education(self, obj):
        return [s.acadamic_level for s in Education.objects.filter(bio_data=obj).order_by('-id')[:2]]

    def political_background(self, obj):
        return [s.description for s in Political_background.objects.filter(bio_data=obj).order_by('-id')[:2]]

    def work_experience(self, obj):
        return [s.role for s in Work_experience.objects.filter(bio_data=obj).order_by('-id')[:2]]

    def activity(self, obj):
        return [s.role for s in Activity.objects.filter(bio_data=obj).order_by('-id')[:2]]
        
    def travel(self, obj):
        return [s.description for s in Travel.objects.filter(bio_data=obj).order_by('-id')[:2]]

    def international_program(self, obj):
        return [s.description for s in International_program.objects.filter(bio_data=obj).order_by('-id')[:2]]

    def publication(self, obj):
        return [s.description for s in Publication.objects.filter(bio_data=obj).order_by('-id')[:2]]

    def skill(self, obj):
        return [s.description for s in Skill.objects.filter(bio_data=obj).order_by('-id')[:2]]

class AchievementAdmin(admin.ModelAdmin):
    formfield_overrides = form_field

    fields = ('title', 'count', 'image', 'image_tag', 'status', 'created')
    readonly_fields = ('created', 'image_tag' )
    list_display = ('title', 'count', 'status', 'image_tag', 'created')
    list_filter = ('status', )

    list_per_page = 10

class SliderAdmin(admin.ModelAdmin):
    formfield_overrides = form_field

    fields = ('caption', 'image', 'image_tag', 'status', 'created')
    readonly_fields = ('created', 'image_tag')
    list_display = ('caption', 'image_tag', 'status', 'created')
    list_filter = ('status', )

    list_per_page = 10

    
class Mainmenu_backgroundAdmin(admin.ModelAdmin):
    formfield_overrides = form_field

    fields = ('logo','logo_image', 'background', 'background_image', 'achievement', 'achievement_image', 'slider', 'slider_image', 'contact', 'contact_image' , 'status')
    readonly_fields = ('logo_image', 'background_image', 'achievement_image', 'slider_image', 'contact_image')
    list_display = ('id', 'logo_image', 'background_image', 'achievement_image', 'slider_image', 'contact_image', 'status')
    list_filter = ('status', )

    list_per_page = 10


admin.site.register(Album, AlbumAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Contact_us, ContactAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Mainmenu, MainMenuAdmin)
admin.site.register(Video_category, VideoCategoryAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Biography, BioDataAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Achievements_counter, AchievementAdmin)
admin.site.register(Mainmenu_background, Mainmenu_backgroundAdmin)