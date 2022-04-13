from django.urls import path

from CarDiary.web.views import CarRegistrationView, show_dashboard

urlpatterns = (
    path('', show_dashboard, name='dashboard'),
    path('add-car/', CarRegistrationView.as_view(), name='add_car'),
)
