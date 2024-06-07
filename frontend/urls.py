from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("seletore/", views.seletore, name="seletore"),
    path("analizzatore/", views.analizzatore, name="analizzatore"),
]