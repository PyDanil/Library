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

        # Создаем авторов с описаниями
        authors_data = [
            (1, 'Николай', 'Гоголь', date(1809, 4, 1), 'Россия', 
             'Великий русский писатель, драматург, поэт, критик, публицист, признанный одним из классиков русской литературы. Автор бессмертных произведений "Мертвые души", "Ревизор", "Вечера на хуторе близ Диканьки".'),
            (2, 'Иван', 'Гончаров', date(1812, 6, 18), 'Россия',
             'Русский писатель и литературный критик. Член-корреспондент Петербургской академии наук по разряду русского языка и словесности, действительный статский советник. Автор романов "Обломов", "Обрыв".'),
            (5, 'Александр', 'Пушкин', date(1799, 6, 6), 'Россия',
             'Великий русский поэт, драматург и прозаик, заложивший основы русского реалистического направления, критик и теоретик литературы, историк, публицист; один из самых авторитетных литературных деятелей первой трети XIX века.'),
        ]
        
        for id_author, first_name, last_name, birthday, country, description in authors_data:
            Author.objects.get_or_create(id_author=id_author, defaults={
                'first_name': first_name, 
                'last_name': last_name, 
                'birthday': birthday, 
                'country': country,
                'description': description
            })

        # Создаем книги с текстом
        books_data = [
            (1, 'Мертвые души', 1, 1842, 1, '/books/gogol/mertvye_dushi.pdf', 2048576, 352, '12+',
             "Глава первая\n\nВ ворота гостиницы губернского города NN въехала довольно красивая рессорная небольшая бричка, в какой ездят холостяки..."),
        ]
        
        for id_book, title, author_id, year, genre_id, file_path, file_size, pages, age_rating, content in books_data:
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
                'age_rating': age_rating,
                'content': content
            })

        self.stdout.write(self.style.SUCCESS('База данных заполнена тестовыми данными!'))