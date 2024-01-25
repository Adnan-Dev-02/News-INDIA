from django.urls import path
from . import views
urlpatterns=[
    path('index/', views.index),
    path('home/', views.index),
    path('about/', views.about),
    path('contact/', views.contact),
    path('video/', views.video),
    path('details/', views.ndetails),
    path('vdetail/', views.vdetails),
    path('news/', views.news),
    path('gallery/', views.gallery),
    path('viewnews/', views.viewnews),
    path('', views.index),
]