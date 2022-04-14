from django.contrib import admin

from CarDiary.auth_app.models import Profile
from CarDiary.web.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):

    list_display = ('make', 'model', 'year')