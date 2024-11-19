from django.urls import include, path
from rest_framework import routers

from expenses.views import ExpenseViewSet

default_router = routers.DefaultRouter()

default_router.register(r"", ExpenseViewSet, basename="expenses")


urlpatterns = [path("expenses/", include(default_router.urls))]
