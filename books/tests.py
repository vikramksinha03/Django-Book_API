from django.test import TestCase
from django.urls import reverse
from .models import Book
# Create your tests here.

class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title = 'A good title', 
            subtitle = 'An excellent subtitle', 
            author = 'Charlie', 
            isbn = '2334738563838',
        )
    
    def test_book_content(self):
        self.assertEqual(self.book.title, 'A good title')
        self.assertEqual(self.book.subtitle, 'An excellent subtitle')
        self.assertEqual(self.book.author, 'Charlie')
        self.assertEqual(self.book.isbn, '2334738563838')

    def test_book_listview(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'An excellent subtitle')
        self.assertTemplateUsed(response, 'books/book_list.html')
