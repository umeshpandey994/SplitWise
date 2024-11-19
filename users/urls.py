from django.urls import include, path
from rest_framework import routers

from users.views import BalanceDataViewSet, UserViewSet

default_router = routers.DefaultRouter()

default_router.register(r"users", UserViewSet, basename="users")
default_router.register(r"balance", BalanceDataViewSet, basename="balance")


urlpatterns = [
    path("", include(default_router.urls)),
]
