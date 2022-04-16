from django.contrib import admin

from CarDiary.auth_app.models import Profile, CarDiaryUser


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(CarDiaryUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)