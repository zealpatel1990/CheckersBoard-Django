from django.contrib import admin
from django.urls import path, re_path
from .views import *
#homeview,signupview, loginview,logoutview

import logging
logger = logging.getLogger("mylogger")

urlpatterns = [
    path('', homeview, name='home'),
    path('signup/',signupview.as_view(), name='signup'),
    path('login/',loginview.as_view(), name='login'),
    re_path(r'/logout/',logoutview.as_view(), name='logout'), # regex will match if there is logot in url it will execute logout in views
    path('ai_game/', ai_game.as_view(), name='ai_game'),
    path('game/', game.as_view(), name='game'),
    path('rules/', rulesview.as_view(), name='rules'),
    path('player_stats/', player_statsview.as_view(), name='player_stats'),
    path('game/createGame/', game.create_game, name='create_game'),
    path('game/joinGame/', game.join_game, name='join_game'),
    path('game/resumeGame/', game.resume_game, name='resume_game'),
    path('checkers/ai_game.html', ai_game.as_view(), name='ai_game'), 
    path('game/<str:game_id>/', room.as_view(), name='game-id'),
    path('gameHistory/<str:game_id>/', room.history_room, name='game-id'),
    path('gameForfiet/<str:game_id>/', game.forfiet_game, name='game-id'),
    path('anonymous/', guestview.as_view(), name='anonymous')

]
