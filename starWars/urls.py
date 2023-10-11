from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('characterList', views.listCharacters, name='list'),
    path('uploadCharacter', views.uploadCharacters, name='upload')
]