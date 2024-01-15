from django import forms
from .models import Image
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('Заголовок', 'Изображение')

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']