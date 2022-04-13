from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models
from datetime import date

UserModel = get_user_model()


class Car(models.Model):
    CAR_MAKE_MIN_LENGTH = 2
    CAR_MAKE_MAX_LENGTH = 15

    CAR_MODEL_MIN_LENGTH = 2
    CAR_MODEL_MAX_LENGTH = 15

    ENGINE_SIZE_MIN = 80
    ENGINE_SIZE_MAX = 9000

    HP_MIN = 1
    HP_MAX = 2999

    LAST_SERVICED_KM_MIN = 1
    LAST_SERVICED_KM_MAX = 999999999

    CURRENT_KM_MIN = 1
    CURRENT_KM_MAX = 999999999

    YEAR_MIN = 1800
    YEAR_MAX = date.today().year

    TYPE_SEDAN = 'Sedan'
    TYPE_HATCHBACK = 'Hatchback'
    TYPE_SUV = 'SUV'
    TYPE_PICKUP = 'Pick-up'
    TYPE_VAN = 'Van'
    TYPES = [(x, x) for x in (TYPE_SEDAN, TYPE_HATCHBACK, TYPE_SUV, TYPE_PICKUP, TYPE_VAN)]

    TRANSMISSION_AUTOMATIC = 'Automatic'
    TRANSMISSION_MANUAL = 'Manual'
    TRANSMISSIONS = [(x, x) for x in (TRANSMISSION_MANUAL, TRANSMISSION_AUTOMATIC)]

    make = models.CharField(
        max_length=CAR_MAKE_MAX_LENGTH,
        validators=(
            MinLengthValidator(CAR_MAKE_MIN_LENGTH),
        )
    )

    model = models.CharField(
        max_length=CAR_MODEL_MAX_LENGTH,
        validators=(
            MinLengthValidator(CAR_MODEL_MIN_LENGTH),
        )
    )

    type = models.CharField(
        max_length=max(len(x) for x, _ in TYPES),
        choices=TYPES,
    )

    year = models.IntegerField(
        validators=(MinValueValidator(YEAR_MIN),
                    MaxValueValidator(YEAR_MAX),
                    )
    )

    transmission = models.CharField(
        max_length=max(len(x) for x, _ in TRANSMISSIONS),
        choices=TRANSMISSIONS,
    )

    engine_size_cc = models.IntegerField(
        validators=(
            MinValueValidator(ENGINE_SIZE_MIN),
            MaxValueValidator(ENGINE_SIZE_MAX),
        )
    )

    current_km = models.IntegerField(
        validators=(
            MinValueValidator(CURRENT_KM_MIN),
            MaxValueValidator(CURRENT_KM_MAX),
        )
    )

    last_serviced_at_km = models.IntegerField(
        validators=(
            MinValueValidator(LAST_SERVICED_KM_MIN),
            MaxValueValidator(LAST_SERVICED_KM_MAX),
        )

    )
    horse_power = models.IntegerField(
        validators=(
            MinValueValidator(HP_MIN),
            MaxValueValidator(HP_MAX),
        )
    )

    image_url = models.URLField(
        blank=True,
        null=True,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
