from django.shortcuts import render, redirect

from books_web.books.forms import BookForm
from books_web.books.models import Book


def show_create_form(request, form):
    context = {
        'form': BookForm
    }
    return render(request, 'create.html', context)


def index(request):
    context = {
        'books': Book.objects.all(),
    }
    return render(request, 'index.html', context)


def create_book(request):
    if request.method == 'GET':
        return show_create_form(request, BookForm)
    else:
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return show_create_form(request, form)


def update_book(request, pk):
    pass
