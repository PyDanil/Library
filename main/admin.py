from django.contrib import admin
from .models import Author, Genre, Book, User

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id_author', 'first_name', 'last_name', 'birthday', 'country']
    search_fields = ['first_name', 'last_name']
    list_filter = ['country']

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['id_genre', 'name_genre', 'description']
    search_fields = ['name_genre']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id_book', 'title', 'id_author', 'year', 'id_genre', 'pages', 'age_rating']
    list_filter = ['id_genre', 'year', 'age_rating']
    search_fields = ['title', 'id_author__first_name', 'id_author__last_name']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id_user', 'email', 'first_name', 'last_name', 'date_join', 'favourite_id_author']
    search_fields = ['first_name', 'last_name', 'email']