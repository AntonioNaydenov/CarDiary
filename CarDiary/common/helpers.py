from django import forms

from CarDiary.web.models import Car


class BootstrapFormMixin:
    fields = {}

    def _init_bootstrap_form_controls(self):
        for _, field in self.fields.items():
            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += ' form-control'


def get_next_car_to_service(cars):
    last_serviced_before = Car.LAST_SERVICED_KM_MIN
    next_car_for_service = None
    for car in cars:
        service_km_margin = car.current_km - car.last_serviced_at_km
        if service_km_margin > last_serviced_before:
            next_car_for_service = car
            last_serviced_before = service_km_margin

    return next_car_for_service
