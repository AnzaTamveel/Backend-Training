from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .models import Course, Instructor, Testimonial
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.conf import settings
from django.template.loader import render_to_string
from .utils import generate_token
from django.core.mail import EmailMessage
from .models import CustomUser , Category , TeamMember

def send_activation_email(request, user):
    current_site = get_current_site(request)
    email_subject = 'Activate your account'
    email_body = render_to_string('account_activation_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user),
    })
    
    email = EmailMessage(
        subject=email_subject,
        body=email_body,
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email]
    )
    email.send()

def activate_user(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (DjangoUnicodeDecodeError, User.DoesNotExist):
        user = None
    
    if user is not None and generate_token.check_token(user, token):
        user.is_email_validated = True
        user.save()
        messages.success(request, "Account activated successfully! You can now log in.")
        return redirect('login')
    
    messages.error(request, "Activation link is invalid!")
    return redirect('signup')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Simple validation
        if not username or not email or not password:
            messages.error(request, "All fields are required.")
            return render(request, 'signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return render(request, 'signup.html')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Send activation email
        send_activation_email(request, user)
        messages.success(request, "Account created successfully! Please check your email to activate your account.")
        return redirect('login')

    return render(request, 'signup.html')
  

def search(request):
    query = request.GET.get('q')
    category_name = request.GET.get('category')
    courses = Course.objects.all() 

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
    courses = Course.objects.all()[:3]
    testimonials = Testimonial.objects.all()
    categories = Category.objects.all()

    return render(request, 'index.html', {
        'courses': courses,
        'testimonials': testimonials,
        'categories': categories,
    })

def courses(request):
    all_courses = Course.objects.all()
    categories = Category.objects.all()

    return render(request, 'courses.html', {
        'courses': all_courses,
        'categories': categories,
    })

def team(request):
    team_members = TeamMember.objects.all()
    return render(request, 'team.html', {'team_members': team_members})

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
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_email_validated:
                auth_login(request, user)
                return redirect('index')  # Redirect to a page you want to show after login
            else:
                messages.error(request, "Please validate your email address.")
                return render(request, 'login.html')

        messages.error(request, "Invalid credentials")
        return render(request, 'login.html')

    return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    return redirect('index')


def single(request):
    return render(request, 'single.html')


