from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy
#from django.contrib.auth.models import User

from .models import AppUser



class RegisterForm(UserCreationForm):
    # email = forms.EmailField(required = True)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['password1'].label = 'password1 label'
        self.fields['password2'].label = gettext_lazy('Repeat Password')

        # self.fields['password1'].help_text = 'password1 help_text'
        # self.fields['password2'].help_text = 'password2 help_text'

        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'First Name'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Repeat Password'})
    
    class Meta:
        model = AppUser
        fields = ['username', 'email', 'first_name', 'password1', 'password2']