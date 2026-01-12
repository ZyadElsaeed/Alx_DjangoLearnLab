# Create a Book Instance

## Command
```python
from bookshelf.models import Book

# Create a new book
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

# Verify creation
Book.objects.all()


<QuerySet [<Book: Book object (1)>]>
