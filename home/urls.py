from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("signup", views.signup, name='signup'),
    path("login", views.loginUser, name='login'),
    path("logout", views.logoutUser, name='logout'),
    path("foryou", views.foryou, name='foryou'),
    path("starcorner", views.starcorner, name='starcorner'),
    path("activities", views.activities, name='activities'),
    path("learning", views.learning, name='learning'),
]