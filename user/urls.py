from django.urls import path

from .views import user_view, UserRegisterView, UserLoginView, UserLogoutView, ProfileUser, UserForgotPasswordView, UserPasswordResetConfirmView

app_name = 'user'

urlpatterns = [
    path('', user_view, name='user_list'),
    path('login/', UserLoginView.as_view(), name='login'),   
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', ProfileUser.as_view(), name='profile'),
    path('password-reset/', UserForgotPasswordView.as_view(), name='password_reset'),
    path('set-new-password/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]