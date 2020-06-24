from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("taqi/", views.taqi, name="taqi"),
    path("<str:name>", views.greet, name="greet")
]