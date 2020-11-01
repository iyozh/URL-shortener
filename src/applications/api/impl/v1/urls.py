from django.urls import include, path
from rest_framework.routers import DefaultRouter

from applications.api.impl.v1.views import LinkViewSet
from applications.api.impl.v1.views.hit_viewset import HitViewSet
from applications.api.impl.v1.views.utm_viewset import UtmViewSet

router = DefaultRouter()

router.register("link", LinkViewSet, "link")
router.register("utm", UtmViewSet, "utm")
router.register("hit", HitViewSet, "hit")

urlpatterns = [path("", include(router.urls))]
