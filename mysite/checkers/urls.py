from django.contrib import admin
from django.urls import path
from .views import *
#homeview,signupview, loginview,logoutview

urlpatterns = [
    path('', homeview, name='home'),
    path('signup/',signupview, name='signup'),
    path('login/',loginview, name='login'),
    path('logout/',logoutview, name='logout'),
    path('game/', game.as_view(), name='game'),
    path('rules/', rulesview, name='rules'),
    path('player_stats', player_statsview, name='player_stats'),

]