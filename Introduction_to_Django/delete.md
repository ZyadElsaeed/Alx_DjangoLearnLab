# Delete a Book Instance

## Command
```python
from bookshelf.models import Book

# Get the book to delete
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Verify deletion
Book.objects.all()

<QuerySet []>
