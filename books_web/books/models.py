from django.core.validators import MinValueValidator
from django.db import models

from books_web.books.validators import validate_pages


class Book(models.Model):
    title = models.CharField(
        max_length=20,
    )
    pages = models.IntegerField(
        validators=[MinValueValidator(1)],
        default=1,
    )

    description = models.CharField(
        max_length=100,
        default='',
    )
    author = models.CharField(
        max_length=20,
    )
