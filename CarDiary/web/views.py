from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from CarDiary.common.view_mixins import RedirectToDashboard
from CarDiary.web.forms import CarRegistrationForm
from CarDiary.web.models import Car


def show_dashboard(request):

    cars = list(Car.objects.filter(user_id=request.user.id))

    context = {
        'cars': cars
    }
    return render(request, 'main/dashboard.html', context)


class CarRegistrationView(views.CreateView):
    form_class = CarRegistrationForm
    template_name = 'main/add-car.html'
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
