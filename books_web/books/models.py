from django.core.validators import MinValueValidator
from django.db import models

from books_web.books.validators import validate_pages


class Book(models.Model):
    title = models.CharField(
        max_length=20,
    )
    pages = models.IntegerField(
        default=0,
        validators=[validate_pages]
    )

    description = models.CharField(
        max_length=100,
        default='',
    )
    author = models.CharField(
        max_length=20,
    )
