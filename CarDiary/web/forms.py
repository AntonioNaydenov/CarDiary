from django import forms

from CarDiary.common.helpers import BootstrapFormMixin, DisabledFieldsFormMixin
from CarDiary.web.models import Car


class CarRegistrationForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        car = super().save(commit=False)
        car.user = self.user
        if commit:
            car.save()
        return car

    class Meta:
        model = Car
        fields = ('make', 'model', 'type', 'year', 'transmission',
                  'engine_size_cc', 'current_km', 'horse_power', 'image_url',
                  'description', 'last_serviced_at_km')


class CarEditForm(BootstrapFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Car
        exclude = ('user',)


class CarDeleteForm(BootstrapFormMixin, DisabledFieldsFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Car
        exclude = ()
        fields = ()
