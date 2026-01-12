# Update a Book Instance

## Command
```python
from bookshelf.models import Book

# Get the book we created
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Verify update
Book.objects.get(id=book.id)

<Book: Nineteen Eighty-Four>
