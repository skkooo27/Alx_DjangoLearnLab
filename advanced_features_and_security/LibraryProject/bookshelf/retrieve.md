# Retrieve Operation

**Command:**
```python
from bookshelf.models import Book
book = Book.objects.get(id=1)
print('Title:', book.title, 'Author:', book.author, 'Year:', book.publication_year)
```

**Output:**
```
Title: 1984 Author: George Orwell Year: 1949
