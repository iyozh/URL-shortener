from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import FormView
from rest_framework.authtoken.models import Token
from applications.onboarding.forms import SignUpForm
from applications.onboarding.models import Profile


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
        Token.objects.create(user=user)
        profile = Profile(user=user, birth_date=birth_date, location=location)
        profile.save()

        return super().form_valid(form)
