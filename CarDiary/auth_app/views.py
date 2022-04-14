from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.views import generic as views
import math

from CarDiary.auth_app.forms import CreateProfileForm, DeleteProfileForm
from CarDiary.auth_app.models import Profile
from CarDiary.common.helpers import get_next_car_to_service
from CarDiary.common.view_mixins import RedirectToDashboard
from CarDiary.web.models import Car


class UserRegisterView(RedirectToDashboard, views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('login page')


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLogoutView(auth_views.LogoutView):
    pass


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'accounts/profile-details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        cars = list(Car.objects.filter(user_id=self.object.user_id))
        next_car_for_service = get_next_car_to_service(cars)

        context.update({
            'cars': cars,
            'cars_count': len(cars),
            'next_car_to_service': next_car_for_service
        })

        return context


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'accounts/password-change.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('dashboard')


def delete_profile_view(request):
    profile = request.user

    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DeleteProfileForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/delete-profile-page.html', context)


