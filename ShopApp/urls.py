from tkinter.font import names

from django.contrib import admin
from django.urls import path
from ShopApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('gallery/', views.images,name='gallery'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('product/', views.product,name='product'),


]
