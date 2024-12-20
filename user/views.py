from django.shortcuts import render
from django.views.generic import DetailView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

# from orders.models import Order
from .forms import UserRegisterForm, UserLoginForm, ProfileUserForm, UserForgotPasswordForm, UserSetNewPasswordForm

@login_required
def user_view(request):
    template_name = "user/user_list.html"
    return render(request, template_name, {})

class UserRegisterView(SuccessMessageMixin, CreateView):
    """ Представление регистрации на сайте с формой регистрации  """
    form_class = UserRegisterForm
    success_url = reverse_lazy('user:login')
    template_name = 'user/user_register.html'
    success_message = 'Вы успешно зарегистрировались. Можете войти на сайт!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация на сайте'
        return context

class UserLoginView(SuccessMessageMixin, LoginView):
    """ Авторизация на сайте """
    form_class = UserLoginForm
    template_name = 'user/user_login.html'
    next_page = 'user:profile'
    success_message = 'Добро пожаловать на сайт!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация на сайте'
        return context

class UserLogoutView(LogoutView):
    """ Выход """
    next_page = 'main:main_list'

class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'user/user_profile.html'
    extra_context = {'title': "Профиль пользователя"}
    success_url = reverse_lazy('user:profile')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

    def get_object(self, queryset=None):
        return self.request.user


class UserForgotPasswordView(SuccessMessageMixin, PasswordResetView):
    """ Представление по сбросу пароля по почте """
    form_class = UserForgotPasswordForm
    template_name = 'user/user_password_reset.html'
    success_url = reverse_lazy('main:main_list')
    success_message = 'Письмо с инструкцией по восстановлению пароля отправлена на ваш email'
    subject_template_name = 'user/email/password_subject_reset_mail.txt'
    email_template_name = 'user/email/password_reset_mail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Запрос на восстановление пароля'
        return context

class UserPasswordResetConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    """ Представление установки нового пароля """
    form_class = UserSetNewPasswordForm
    template_name = 'user/user_password_set_new.html'
    success_url = reverse_lazy('main:main_list')
    success_message = 'Пароль успешно изменен. Можете авторизоваться на сайте.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Установить новый пароль'
        return context
