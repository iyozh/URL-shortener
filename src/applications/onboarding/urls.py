from django.urls import path, re_path

from applications.onboarding.apps import OnboardingConfig
from applications.onboarding.views import SignInView, SignUpView

app_name = OnboardingConfig.label

urlpatterns = [
    path("sign-in/", SignInView.as_view(), name="sign-in"),
    path("sign-up/", SignUpView.as_view(), name="sign-up"),
]
