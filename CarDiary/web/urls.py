from django.urls import path

from CarDiary.web.views import show_index, register_page, login_page

urlpatterns = (
    path('', show_index, name='home page'),
    path('register/', register_page, name='register page'),
    path('login/', login_page, name='login page'),
)
