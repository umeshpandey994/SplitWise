from django.urls import include, path
from rest_framework import routers

from users.views import UserViewSet

default_router = routers.DefaultRouter()
default_router.register(r"", UserViewSet, basename="users")

urlpatterns = [
    path("users/", include(default_router.urls)),
]
