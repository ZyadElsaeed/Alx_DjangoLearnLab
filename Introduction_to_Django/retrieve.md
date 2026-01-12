# Retrieve Book Instances

## Command
```python
from bookshelf.models import Book

# Retrieve all books
Book.objects.all()

# Retrieve specific book by title
Book.objects.get(title="1984")

# All books
<QuerySet [<Book: Book object (1)>]>

# Specific book
<Book: 1984>
