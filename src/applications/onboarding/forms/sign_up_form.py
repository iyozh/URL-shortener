from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django_countries.fields import CountryField

User = get_user_model()


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    location = CountryField().formfield(label="Country")
    birth_date = forms.DateField(label="Birth date", widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

