from django.urls import path
from . import views

urlpatterns = [
    path('', views.user),
    path('add_comment/',views.add_comment),
    path('add_star/',views.add_star),
    path('add_fav/',views.add_fav),
    path('remove_fav/',views.remove_fav),
    path('register/',views.register),
    path('login/',views.login), 
    path('sendEmailCode/',views.sendEmailCode), 
]