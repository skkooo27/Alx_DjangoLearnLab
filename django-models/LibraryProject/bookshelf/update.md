# Update Operation

**Command:**
```python
from bookshelf.models import Book
book = Book.objects.get(id=1)
book.title = 'Nineteen Eighty-Four'
book.save()
print('Updated title to:', book.title)
```

**Output:**
```
Updated title to: Nineteen Eighty-Four
