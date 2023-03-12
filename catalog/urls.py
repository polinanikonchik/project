from django.contrib import admin
from django.urls import path, include
from .views import IndexView, BookView, AuthorsView, AuthorView, GenresView, GenreView, SearchView

# '' - домашняя страница
# books/ - список всех книг
# authors/ - список всех авторов
# catalog/<id> детальная информация для определенной книги
# author/<id> - детальная инфа для определенного автора
urlpatterns = [
    path('', IndexView.as_view(), name='catalog-index'),
    path('authors/', AuthorsView.as_view(), name='catalog-authors'),
    path('catalog/genres/', GenresView.as_view(),name= 'catalog-genres' ),
    path('catalog/<int:id>/',BookView.as_view(),name = 'catalog-book'),
    path('catalog/<str:first_name>-<str:last_name>/',AuthorView.as_view(), name='catalog-author'),
    path('catalog/genres/<str:name>/',GenreView.as_view(),name= 'catalog-genre'),
    path('catalog/search/',SearchView.as_view(),name='catalog-search')
]
