from django.shortcuts import render
from .models import BookInfo


def explore(request):
    books = BookInfo.objects.all()
    return render(request, 'base.html', {'books': books})


def find(request):
    books = BookInfo.objects.all()

    if request.method == 'POST':
        search_title = request.POST.get('search_title')
        if search_title:
            books = books.filter(title__icontains=search_title)

    return render(request, 'book_list.html', {'books': books})