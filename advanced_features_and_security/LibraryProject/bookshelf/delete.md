# Delete Operation

**Command:**
```python
from bookshelf.models import Book
book = Book.objects.get(id=1)
book.delete()
print('Book deleted')
books = Book.objects.all()
print('Remaining books:', list(books))
```

**Output:**
```
Book deleted
Remaining books: []
