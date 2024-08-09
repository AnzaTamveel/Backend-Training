from django.shortcuts import render
from .models import Book, Author, Publisher, Store, Stock

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})

def publisher_list(request):
    publishers = Publisher.objects.all()
    return render(request, 'publisher_list.html', {'publishers': publishers})

def store_list(request):
    stores = Store.objects.all()
    return render(request, 'store_list.html', {'stores': stores})

def home(request):
    return render(request, 'home.html')

