from django.core.management.base import BaseCommand
from main.models import Author, Genre, Book, User
from datetime import date

class Command(BaseCommand):
    help = 'Fill database with test data'

    def handle(self, *args, **options):
        # Создаем жанры
        genres_data = [
            (1, 'Роман', 'крупное повествовательное произведение со сложным сюжетом'),
            (2, 'Поэма', 'крупное стихотворное произведение с повествовательным сюжетом'),
            (3, 'Пьеса', 'Драматическое произведение для театральной постановки'),
            (4, 'Классика', 'Произведения, признанные образцовыми в мировой литературе'),
        ]
        
        for id_genre, name, desc in genres_data:
            Genre.objects.get_or_create(id_genre=id_genre, defaults={'name_genre': name, 'description': desc})

        # Создаем авторов
        authors_data = [
            (1, 'Николай', 'Гоголь', date(1809, 4, 1), 'Россия'),
            (2, 'Иван', 'Гончаров', date(1812, 6, 18), 'Россия'),
            (5, 'Александр', 'Пушкин', date(1799, 6, 6), 'Россия'),
        ]
        
        for id_author, first_name, last_name, birthday, country in authors_data:
            Author.objects.get_or_create(id_author=id_author, defaults={
                'first_name': first_name, 
                'last_name': last_name, 
                'birthday': birthday, 
                'country': country
            })

        # Создаем книги
        books_data = [
            (1, 'Мертвые души', 1, 1842, 1, '/books/gogol/mertvye_dushi.pdf', 2048576, 352, '12+'),
            (2, 'Обломов', 2, 1859, 1, '/books/goncharov/oblomov.pdf', 3072000, 490, '12+'),
            (5, 'Евгений Онегин', 5, 1833, 2, '/books/pushkin/evgeny_onegin.pdf', 1530600, 240, '12+'),
        ]
        
        for id_book, title, author_id, year, genre_id, file_path, file_size, pages, age_rating in books_data:
            author = Author.objects.get(id_author=author_id)
            genre = Genre.objects.get(id_genre=genre_id)
            Book.objects.get_or_create(id_book=id_book, defaults={
                'title': title,
                'id_author': author,
                'year': year,
                'id_genre': genre,
                'file_path': file_path,
                'file_size': file_size,
                'pages': pages,
                'age_rating': age_rating
            })

        self.stdout.write(self.style.SUCCESS('База данных заполнена тестовыми данными!'))