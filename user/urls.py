from django.urls import path

from .views import user_view, UserRegisterView, UserLoginView, UserLogoutView, ProfileUser

app_name = 'user'

urlpatterns = [
    path('', user_view, name='user_list'),

    path('login/', UserLoginView.as_view(), name='login'),   
    path('logout/', UserLogoutView.as_view(), name='logout'),
    
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', ProfileUser.as_view(), name='profile'),
]