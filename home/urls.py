from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path('', views.index, name='home'),
    path('shop', views.shop, name='shop'),
    path('about', views.about, name='about'),
    path('categories', views.categories, name='categories'),
    path('contact', views.contact, name='contact'),

]
