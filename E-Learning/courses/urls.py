from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),
    path('contact/', views.contact, name='contact'),
    path('instructor/', views.instructor, name='instructor'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('single/', views.single, name='single'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('search/', views.search, name='search'),

]
