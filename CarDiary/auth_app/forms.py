from django import forms

from CarDiary.auth_app.models import Profile
from CarDiary.common.helpers import BootstrapFormMixin
from django.contrib.auth import forms as auth_forms, get_user_model


class CreateProfileForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LENGTH,
    )
    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LENGTH,
    )
    image = forms.URLField()

    email = forms.EmailField()

    gender = forms.ChoiceField(
        choices=Profile.GENDERS,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            image=self.cleaned_data['image'],
            email=self.cleaned_data['email'],
            gender=self.cleaned_data['gender'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name',
                  'image', 'gender',)
        widgets = {
                'first_name': forms.TextInput(
                    attrs={
                        'placeholder': 'Enter first name',
                    }
                ),
                'last_name': forms.TextInput(
                    attrs={
                        'placeholder': 'Enter last name',
                    }
                ),
                'image': forms.TextInput(
                    attrs={
                        'placeholder': 'Enter URL',
                    }
                ),
        }


class EditProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.initial['gender'] = Profile.DO_NOT_SPECIFY

    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name',
                }
            ),
            'image': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter email',
                }
            ),


        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()
