from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Course, Instructor, Testimonial

def search(request):
    query = request.GET.get('q')  # Search query from search input (if any)
    category_name = request.GET.get('category')  # Get the category name from the URL
    courses = Course.objects.all()  # Initially fetch all courses

    if category_name:
        # Filter courses by the selected category
        courses = courses.filter(category__name__icontains=category_name)

    elif query:
        # If no category, filter by search query
        courses = courses.filter(title__icontains=query) | courses.filter(category__name__icontains=query)

    context = {
        'courses': courses,
        'category_name': category_name if category_name else query,
    }
    return render(request, 'search.html', context)

def index(request):
    courses = Course.objects.all()[:3]  # Display top 3 courses
    testimonials = Testimonial.objects.all()
    return render(request, 'index.html', {'courses': courses, 'testimonials': testimonials})

def courses(request):
    all_courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': all_courses})

def instructor(request):
    instructors = Instructor.objects.all()
    return render(request, 'instructor.html', {'instructors': instructors})

def testimonial(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'testimonial.html', {'testimonials': testimonials})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            auth_login(request, user)
            return redirect('index')  # Redirect to the home page after signup
    return render(request, 'signup.html')

def logout(request):
    auth_logout(request)
    return redirect('index')


def single(request):
    return render(request, 'single.html')


def team(request):
    return render(request, 'team.html')

