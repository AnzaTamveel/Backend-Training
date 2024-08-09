# bookstore/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('authors/', views.author_list, name='author_list'),
    path('publishers/', views.publisher_list, name='publisher_list'),
    path('stores/', views.store_list, name='store_list'),
]
