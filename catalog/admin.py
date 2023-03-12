from django.contrib import admin
from .models import Book, Author, Genre


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death', 'photo')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'price', 'image')


# admin.site.register(Book, BookAdmin)
# admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
