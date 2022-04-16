from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixin

from CarDiary.common.view_mixins import RedirectToDashboard
from CarDiary.web.forms import CarRegistrationForm, CarDeleteForm, CarEditForm
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


class CarDetailsView(auth_mixin.LoginRequiredMixin, views.DetailView):
    model = Car
    template_name = 'main/car-details.html'
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        km_without_service = self.object.current_km - self.object.last_serviced_at_km

        context.update({
            'km_without_service': km_without_service
        })

        return context


class CarEditView(views.UpdateView):
    model = Car
    template_name = 'main/edit-car.html'
    form_class = CarEditForm
    success_url = reverse_lazy('dashboard')


class CarDeleteView(views.DeleteView):
    model = Car
    template_name = 'main/car-delete.html'
    form_class = CarDeleteForm
    success_url = reverse_lazy('dashboard')





