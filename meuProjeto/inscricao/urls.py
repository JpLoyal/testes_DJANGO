from django.urls import path

from . import views

urlpatterns = [
    path('', views.mostra_formulario),
]