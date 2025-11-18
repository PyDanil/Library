from django.shortcuts import render, get_object_or_404
from .models import Book, Author, Genre, User

def book_list(request):
    books = Book.objects.all().select_related('id_author', 'id_genre')
    genres = Genre.objects.all()
    
    genre_filter = request.GET.get('genre')
    if genre_filter:
        books = books.filter(id_genre=genre_filter)
    
    search_query = request.GET.get('search')
    if search_query:
        books = books.filter(title__icontains=search_query)
    
    context = {
        'books': books,
        'genres': genres,
        'selected_genre': genre_filter,
        'search_query': search_query or ''
    }
    return render(request, 'main/book_list.html', context)

def book_detail(request, book_id):
    book = get_object_or_404(Book.objects.select_related('id_author', 'id_genre'), id_book=book_id)
    return render(request, 'main/book_detail.html', {'book': book})

def book_read(request, book_id):
    book = get_object_or_404(Book.objects.select_related('id_author', 'id_genre'), id_book=book_id)
    return render(request, 'main/book_read.html', {'book': book})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'main/author_list.html', {'authors': authors})

def author_detail(request, author_id):
    author = get_object_or_404(Author, id_author=author_id)
    author_books = Book.objects.filter(id_author=author).select_related('id_genre')
    return render(request, 'main/author_detail.html', {
        'author': author,
        'books': author_books
    })

def user_list(request):
    users = User.objects.all().select_related('favourite_id_author')
    return render(request, 'main/user_list.html', {'users': users})