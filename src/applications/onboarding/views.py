from django import forms
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import FormView
from django_countries.fields import CountryField

from applications.onboarding.models import Profile

User = get_user_model()


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    location = CountryField().formfield(label="Country")
    birth_date = forms.DateField(label="Birth date")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class SignInView(LoginView):
    template_name = "onboarding/sign-in.html"


class SignUpView(FormView):
    template_name = "onboarding/sign-up.html"
    form_class = SignUpForm
    success_url = reverse_lazy("homepage:index")

    def form_valid(self, form):
        form.save()

        username = form.cleaned_data["username"]
        password = form.cleaned_data["password1"]
        birth_date = form.cleaned_data["birth_date"]
        location = form.cleaned_data["location"]

        user = authenticate(self.request, username=username, password=password)
        login(self.request, user)
        profile = Profile(user=user, birth_date=birth_date, location=location)
        profile.save()

        return super().form_valid(form)
