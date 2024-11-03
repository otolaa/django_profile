from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.forms.widgets import ClearableFileInput

class CustomClearableFileInput(ClearableFileInput):
    template_name = "user/widgets/custom_clearable_file_input.html"

class UserUpdateForm(forms.ModelForm):
    """ Форма обновления данных пользователя """
    class Meta:
        model = get_user_model()
        fields = ('photo', 'username', 'email', 'date_birth', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        """  Обновление стилей формы под bootstrap  """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    def clean_email(self):
        """ Проверка email на уникальность  """
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        user_model = get_user_model()
        if email and user_model.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('Email адрес должен быть уникальным')
        return email

class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label='Логин', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    email = forms.CharField(disabled=True, label='E-mail', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    photo = forms.ImageField(label='Аватар', required=False, widget=CustomClearableFileInput(attrs={'class': 'form-control form-control-lg'}))
  
    class Meta:
        model = get_user_model()
        fields = ['photo', 'username', 'email', 'date_birth', 'first_name', 'last_name', 'telegram', 'vk', 'twitter']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }
        widgets = {
            'date_birth': forms.DateInput(attrs={'class': 'form-control form-control-lg'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'telegram': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'vk': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'twitter': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
        }

class UserRegisterForm(UserCreationForm):
    """ Переопределенная форма регистрации пользователей """
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        # email = forms.EmailField(required=True)
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name')

    def clean_email(self):
        """ Проверка email на уникальность """
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        user_model = get_user_model()
        if email and user_model.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('Такой email уже используется в системе')
        return email

    def __init__(self, *args, **kwargs):
        """ Обновление стилей формы регистрации """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['username'].widget.attrs.update({"placeholder": 'Придумайте свой логин'})
            self.fields['email'].widget.attrs.update({"placeholder": 'Введите свой email'})
            self.fields['email'].widget.attrs['required'] = 'required'
            self.fields['first_name'].widget.attrs.update({"placeholder": 'Ваше имя'})
            self.fields["last_name"].widget.attrs.update({"placeholder": 'Ваша фамилия'})
            self.fields['password1'].widget.attrs.update({"placeholder": 'Придумайте свой пароль'})
            self.fields['password2'].widget.attrs.update({"placeholder": 'Повторите придуманный пароль'})
            self.fields[field].widget.attrs.update({"class": "form-control form-control-lg", "autocomplete": "off"})

class UserLoginForm(AuthenticationForm):
    """ Форма авторизации на сайте """
    def __init__(self, *args, **kwargs):
        """ Обновление стилей формы регистрации """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['username'].widget.attrs['placeholder'] = 'Логин пользователя'
            self.fields['password'].widget.attrs['placeholder'] = 'Пароль пользователя'
            self.fields['username'].label = 'Логин'
            self.fields[field].widget.attrs.update({
                'class': 'form-control form-control-lg',
                'autocomplete': 'off'
            })