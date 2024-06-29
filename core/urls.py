from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("work/", views.work, name="work"),
    path("legal/", views.legal, name="legal"),
]