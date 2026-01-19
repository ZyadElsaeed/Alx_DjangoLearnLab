import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        # التعديل: استخدام objects.filter صراحة
        books = Book.objects.filter(author=author)
        for book in books:
            print(book.title)
    except Author.DoesNotExist:
        print("Author not found")

def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        for book in books:
            print(book.title)
    except Library.DoesNotExist:
        print("Library not found")

def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        # التعديل: استخدام Librarian.objects.get صراحة
        librarian = Librarian.objects.get(library=library)
        print(librarian.name)
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        print("Librarian not found")
