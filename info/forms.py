from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields.pop('password2')
        self.fields['email'].required = True
        self.fields['gender'].required = True
        self.fields['mobile_no'].required = True
        self.fields['relation'].required = True
        self.fields['full_name'].required = True
        self.fields['cc_myself'].required = True
    mobile_no = forms.CharField(
        label='Mobile No',
        max_length=10,
        widget=forms.TextInput(attrs={'type': 'tel','pattern':"\\A[0-9]{10}\\z",
                                      'title':"Number should be 10 digit numeric",'placeholder':'Mobile No'}),
        help_text=None,
    )

    password1 = forms.CharField(
        label= "Password",
        strip=False,
        min_length=6,
        widget=forms.PasswordInput(attrs={'placeholder':'Enter Passoword'}),
        help_text=None,
    )
    cc_myself = forms.BooleanField(
        required=True,
        label="<a href='detail/'>Check to agree to agreement</a>"
    )
    class Meta:
        model = User
        fields = ("username","email", "gender","mobile_no","relation","full_name")
        help_texts = {
            'username': None,
            'email': None,
        }

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
