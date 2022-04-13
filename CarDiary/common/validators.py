from django.core.exceptions import ValidationError
VALIDATE_ONLY_LETTERS_ERROR_MESSAGE = 'Value must contain only letters.'


def validate_only_letters(value):
    if not value.isalpha():
        raise ValidationError(VALIDATE_ONLY_LETTERS_ERROR_MESSAGE)
