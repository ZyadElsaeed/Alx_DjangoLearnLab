from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITestCase(APITestCase):
    def setUp(self):
        # إنشاء مستخدم للاختبارات التي تتطلب صلاحيات
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2020,
            author=self.author
        )
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')

    def test_get_books_status_code(self):
        # اختبار قراءة الكتب (يجب أن يعيد 200)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book_authenticated(self):
        # تسجيل الدخول واختبار إنشاء كتاب (يجب أن يعيد 201)
        self.client.login(username='testuser', password='password123')
        data = {
            "title": "New Book",
            "publication_year": 2024,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_book_unauthenticated(self):
        # اختبار الإنشاء بدون تسجيل دخول (يجب أن يعيد 403 بسبب الصلاحيات)
        data = {"title": "Ghost Book", "publication_year": 2024, "author": self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
