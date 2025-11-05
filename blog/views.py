# views.py
from django.shortcuts import render
from .models import Post

def book_list(request):
    cont = Post.objects.all()  # Get all books from the table
    return render(request, 'blog/book_list.html', {'cont': cont})
