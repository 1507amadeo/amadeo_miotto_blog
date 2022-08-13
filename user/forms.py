from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import User
from django.forms import ModelForm
from user.models import Avatar

class UserRegisterForm(UserCreationForm):

    username = forms.CharField(label='Username', min_length=3)
    first_name = forms.CharField(label='Name', min_length=3)
    last_name = forms.CharField(label='Last name', min_length=3)
    email = forms.EmailField(label='e-mail')
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)
    fecha_nacimiento=forms.DateField(
        label='Date of publication',
        widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'})
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2','fecha_nacimiento']
        help_texts = {k: "" for k in fields}


class UserEditForm(UserCreationForm):
    password = None

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'perfil']
        widgets = {
            'email': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
        help_texts = {k: "" for k in fields}



class AvatarForm(ModelForm):
    class Meta:
        model = Avatar
        fields = ('image', )