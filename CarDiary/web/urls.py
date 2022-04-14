from django.urls import path

from CarDiary.web.views import CarRegistrationView, show_dashboard, CarDetailsView, CarDeleteView, CarEditView

urlpatterns = (
    path('', show_dashboard, name='dashboard'),
    path('add-car/', CarRegistrationView.as_view(), name='add_car'),
    path('<int:pk>/', CarDetailsView.as_view(), name='car details'),
    path('car/delete/<int:pk>', CarDeleteView.as_view(), name='car delete'),
    path('car/edit/<int:pk>', CarEditView.as_view(), name='car edit'),
)
