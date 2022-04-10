from django import forms

from CarDiary.auth_app.models import CarDiaryUser


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = CarDiaryUser
        fields = ('username', 'password', 'image')
