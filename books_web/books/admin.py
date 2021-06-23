from django.contrib import admin

from books_web.books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'pages', 'description', 'author']



