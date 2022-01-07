from django.urls import path
from . import views

urlpatterns = [
    path('', views.allmovie),
    path('search/',views.search)
]