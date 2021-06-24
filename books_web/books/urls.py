from django.urls import path

from books_web.books.views import index, create_book, update_book, delete_book

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_book, name='create book'),
    path('update/<int:pk>', update_book, name='update book'),
    path('delete/<int:pk>', delete_book, name='delete book'),

]
