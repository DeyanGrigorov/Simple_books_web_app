from django.core.exceptions import ValidationError


def validate_pages(value):
    if value <= 0:
        raise ValidationError('pages cannot be zero')


