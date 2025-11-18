from django.db import models

class Author(models.Model):
    id_author = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birthday = models.DateField()
    country = models.CharField(max_length=40)
    photo = models.ImageField(upload_to='authors/', blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True)  # новое поле
    
    class Meta:
        db_table = 'Author'
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Genre(models.Model):
    id_genre = models.AutoField(primary_key=True)
    name_genre = models.CharField(max_length=40)
    description = models.CharField(max_length=400)
    
    class Meta:
        db_table = 'Genre'
    
    def __str__(self):
        return self.name_genre

class Book(models.Model):
    id_book = models.AutoField(primary_key=True)
    title = models.CharField(max_length=80)
    id_author = models.ForeignKey(Author, on_delete=models.CASCADE, db_column='id_author')
    year = models.IntegerField()
    id_genre = models.ForeignKey(Genre, on_delete=models.CASCADE, db_column='id_genre')
    file_path = models.CharField(max_length=100)
    file_size = models.IntegerField()
    pages = models.IntegerField()
    age_rating = models.CharField(max_length=10)
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    content = models.TextField(blank=True)  # текст книги
    
    class Meta:
        db_table = 'Book'
    
    def __str__(self):
        return self.title

class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    email = models.CharField(max_length=30)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_join = models.DateField()
    favourite_id_author = models.ForeignKey(Author, on_delete=models.CASCADE, db_column='favourite_id_author')
    
    class Meta:
        db_table = 'User'
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"