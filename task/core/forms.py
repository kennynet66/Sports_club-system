from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Member_details

INPUT_CLASSES = 'w-3/4 py-4 px-6 rounded-xl border mr-5 ml-5'

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Your Username',
        'class' : 'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Your Password',
        'class' : 'w-full py-4 px-6 rounded-xl',
    }))

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Member_details
        fields = ('firstname','lastname','gender', 'name_of_next_of_kin', 'relationship','passport','weight','height')
        widgets = {
            'firstname' : forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'lastname' : forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'gender' : forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name_of_next_of_kin' : forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'relationship' : forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'weight' : forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'height' : forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'passport' : forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),

    }