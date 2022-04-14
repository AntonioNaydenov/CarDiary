from django.urls import path, include

from CarDiary.auth_app.views import UserRegisterView, UserLoginView, ProfileDetailsView, delete_profile_view, \
    ChangePasswordView, UserLogoutView

urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='register page'),
    path('login/', UserLoginView.as_view(), name='login page'),
    path('logout/', UserLogoutView.as_view(), name='log out'),
    path('<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('profile/delete/', delete_profile_view, name='delete profile'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
        )
