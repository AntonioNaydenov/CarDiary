from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import models as auth_models

from CarDiary.auth_app.managers import CarDiaryUserManager
from CarDiary.common.validators import validate_only_letters


class CarDiaryUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LENGTH = 12

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    objects = CarDiaryUserManager()


class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 15
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 20

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SPECIFY = 'Do not specify'

    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SPECIFY)]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    image = models.URLField()

    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=GENDERS,
        null=True,
        blank=True,
        default=DO_NOT_SPECIFY,
    )

    email = models.EmailField(
        null=True,
        blank=True,
        unique=True,
    )

    user = models.OneToOneField(
        CarDiaryUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
