from django.contrib import admin
from django.urls import path, include
from .views import IndexView

# '' - домашняя страница
# books/ - список всех книг
# authors/ - список всех авторов
# book/<id> детальная информация для определенной книги
# author/<id> - детальная инфа для определенного автора
urlpatterns = [
    path('', IndexView.as_view(),name='catalog-index' )
]
