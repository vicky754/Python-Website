
from django.contrib import admin
from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.home),
    path('addUser',v.addUser),
    path('userLogin',v.mylogin),
    path('userLogout',v.logOUT),
    path('getByCategory',v.getByCategory)
]
