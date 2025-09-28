from django.db import models

# Author model: Represents an author with a name field.
# This model establishes a one-to-many relationship with the Book model.
class Author(models.Model):
    name = models.CharField(max_length=100)  # The name of the author

    def __str__(self):
        return self.name

# Book model: Represents a book with title, publication year, and a foreign key to Author.
# The relationship allows an author to have multiple books.
class Book(models.Model):
    title = models.CharField(max_length=200)  # The title of the book
    publication_year = models.IntegerField()  # The year the book was published
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)  # Foreign key to Author

    def __str__(self):
        return self.title
