"""udaya_rana_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from udaya_rana import views

urlpatterns = [
    path('', views.home, name='home'),
    path('photogallery', views.photo_gallery, name='photo_gallery'),
    path('videogallery', views.video_gallery, name="video_gallery"),
    path('article/', views.article, name="article"),
    path('biography', views.biography, name="biography"),
    path('contact_us', views.contact_us, name="contact_us")
]
