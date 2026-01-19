import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        for book in author.books.all():
            print(book.title)
    except Author.DoesNotExist:
        print("Author not found")

def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        for book in library.books.all():
            print(book.title)
    except Library.DoesNotExist:
        print("Library not found")

def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        print(library.librarian.name)
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        print("Librarian not found")
