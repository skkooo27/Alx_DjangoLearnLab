# Create Operation

**Command:**
```python
from bookshelf.models import Book
book = Book.objects.create(title='1984', author='George Orwell', publication_year=1949)
print('Book created with ID:', book.id)
```

**Output:**
```
Book created with ID: 1
