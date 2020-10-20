from django.urls import path

from applications.onboarding.apps import OnboardingConfig
from applications.onboarding.views import SignInView, SignOutView, SignUpView

app_name = OnboardingConfig.label

urlpatterns = [
    path("sign-in/", SignInView.as_view(), name="sign-in"),
    path("sign-up/", SignUpView.as_view(), name="sign-up"),
    path("sign-out/", SignOutView.as_view(), name="sign-out"),
]
