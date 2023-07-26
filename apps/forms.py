from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth.hashers import make_password
from django.forms import ModelForm, CharField

from apps.models import Register


class UpdateForm(UserChangeForm):
    class Meta:
        model = Register
        fields = (
            'first_name', 'last_name', 'mobile_number', 'phone_number', 'facebook', 'instagram', 'dribble', 'skype',
            'twitter', 'image', 'linkedin')


class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = ['username', 'email', 'password']

    def clean_password(self):
        return make_password(self.cleaned_data['password'])


class CustomLoginForm(AuthenticationForm):
    username = CharField(max_length=255)
    password = CharField()
