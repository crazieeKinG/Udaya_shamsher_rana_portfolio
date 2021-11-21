from django.http import HttpResponse
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'index.html')


def photo_gallery(request):
    return render(request, 'photo-gallery.html')


def video_gallery(request):
    return render(request, 'video-gallery.html')


def article(request):
    return render(request, 'article.html')


def biography(request):
    return render(request, 'details.html')
