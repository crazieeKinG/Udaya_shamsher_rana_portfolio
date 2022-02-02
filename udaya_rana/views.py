from types import CoroutineType
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import *
from django.core.paginator import Paginator

def home(request):
    mainmenu = Mainmenu.objects.all().order_by('order_by')
    background = Mainmenu_background.objects.filter(status='active').first()

    albums = Album.objects.filter(status='active').order_by('-created')[:3]
    
    videos = Video.objects.filter(status='active').order_by('-id')[:3]
    
    articles = Article.objects.filter(status='active').order_by('-created')[:3]
    
    bio = Biography.objects.first()
    if bio:
        bio.titles = Title.objects.filter(bio_data=bio)
        bio.records = 1

    achievements = Achievements_counter.objects.all()
    
    slider = Slider.objects.filter(status='active')
    

    context = {
        'mainmenu': mainmenu,
        'background': background,
        'albums': albums,
        'videos': videos,
        'articles': articles,
        'bio_data': bio,
        'achievements': achievements,
        'slider': slider
    }

    return render(request, 'index.html', context=context)


def photo_gallery(request):
    mainmenu = Mainmenu.objects.all().order_by('order_by')
    background = Mainmenu_background.objects.filter(status='active').first()

    albums = Album.objects.filter(status='active').order_by('name')

    bio = Biography.objects.first()

    paginator = Paginator(albums, 9)
    page_number = request.GET.get('page', 1)
    single_page_albums = paginator.get_page(page_number)

    context = {
        'mainmenu': mainmenu,
        'background': background,
        'bio_data' : bio,
        'albums': single_page_albums,
        'current': int(page_number),
        'pages': range(1, (paginator.num_pages+1))
    }
    return render(request, 'photo-gallery.html', context=context)

def photo_collection(request, id, album):
    mainmenu = Mainmenu.objects.all().order_by('order_by')
    background = Mainmenu_background.objects.filter(status='active').first()

    images = Image.objects.filter(status='active', album__id=id).order_by('-created')

    bio = Biography.objects.first()

    paginator = Paginator(images, 9)
    page_number = request.GET.get('page', 1)
    single_page_images = paginator.get_page(page_number)

    context = {
        'mainmenu': mainmenu,
        'background': background,
        'bio_data' : bio,
        'id': id,
        'album': album,
        'images': single_page_images,
        'current': int(page_number),
        'pages': range(1, (paginator.num_pages+1))
    }
    return render(request, 'photo-collection.html', context=context)

def video_gallery(request):
    mainmenu = Mainmenu.objects.all().order_by('order_by')
    background = Mainmenu_background.objects.filter(status='active').first()

    videos = Video_category.objects.filter(status='active').order_by('title')
   
    bio = Biography.objects.first()

    paginator = Paginator(videos, 8)
    page_number = request.GET.get('page', 1)
    single_page_video = paginator.get_page(page_number)

    context = {
        'mainmenu': mainmenu,
        'background': background,
        'bio_data' : bio,        
        'video_category': single_page_video,
        'current': int(page_number),
        'pages': range(1, (paginator.num_pages+1))
    }
    return render(request, 'video-gallery.html', context=context)

def video_collection(request, id, category):
    mainmenu = Mainmenu.objects.all().order_by('order_by')
    background = Mainmenu_background.objects.filter(status='active').first()

    videos = Video.objects.filter(status='active', video_category__id=id).order_by('-created')

    bio = Biography.objects.first()

    paginator = Paginator(videos, 1)
    page_number = request.GET.get('page', 1)
    single_page_videos = paginator.get_page(page_number)

    context = {
        'mainmenu': mainmenu,
        'background': background,
        'bio_data' : bio,
        'id': id,
        'video_category': category,
        'videos': single_page_videos,
        'current': int(page_number),
        'pages': range(1, (paginator.num_pages+1))
    }
    return render(request, 'video-collection.html', context=context)

def article(request):
    mainmenu = Mainmenu.objects.all().order_by('order_by')
    background = Mainmenu_background.objects.filter(status='active').first()

    articles = Article.objects.filter(status='active').order_by('-created')
    
    bio = Biography.objects.first()

    paginator = Paginator(articles, 4)
    page_number = request.GET.get('page', 1)
    single_page_article = paginator.get_page(page_number)

    context = {
        'mainmenu': mainmenu,
        'background': background,
        'bio_data' : bio,
        'articles': single_page_article,        
        'current': int(page_number),
        'pages': range(1, (paginator.num_pages+1))
    }

    return render(request, 'article.html', context=context)


def biography(request):
    mainmenu = Mainmenu.objects.all().order_by('order_by')
    background = Mainmenu_background.objects.filter(status='active').first()

    bio = Biography.objects.first()
    if bio:
        bio.telephone = Telephone.objects.filter(bio_data=bio)
        bio.email = Email.objects.filter(bio_data=bio)
        bio.titles = Title.objects.filter(bio_data=bio)
        education = Education.objects.filter(bio_data=bio)
        political_background = Political_background.objects.filter(bio_data=bio)
        work_experience = Work_experience.objects.filter(bio_data=bio)
        activity = Activity.objects.filter(bio_data=bio)
        travel = Travel.objects.filter(bio_data=bio)
        international_program = International_program.objects.filter(bio_data=bio)
        publication = Publication.objects.filter(bio_data=bio)
        skill = Skill.objects.filter(bio_data=bio)
        context = {
            'mainmenu' : mainmenu,
            'background': background,
            'length': 1,
            'bio_data' : bio,
            'education' : education,
            'political_background' : political_background,
            'work_experience' : work_experience,
            'activity' : activity,
            'travel' : travel,
            'international_program' : international_program,
            'publication' : publication,
            'skill' : skill
        }
    else:
        context = {
            'mainmenu' : mainmenu,
            'background': background,
            'length': 0
        }
        
    return render(request, 'biography.html', context=context)



def contact_us(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        contact_no = request.POST['contact_no']
        message = request.POST['message']

        data = Contact_us(name=name, email=email, message=message, contact_number= contact_no)
        data.save()

    return redirect('home')
