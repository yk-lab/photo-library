from django.urls import path

from . import views
from .apps import CoreConfig

app_name = CoreConfig.name

urlpatterns = [
    path("", views.TopView.as_view(), name="top"),
]
