
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Book

"""
    test_get_books_list: 
    It checks if the endpoint returns a successful response (HTTP 200) and verifies that the number of books returned matches the number of books in the database.

    test_get_books_list_empty: 
    It checks if the API returns a successful response (HTTP 200) and confirms that the response data is an empty list.

"""

class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.books_url = reverse('book-list-create')
        self.book_data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'publication_date': '2023-07-27',
        }
        self.book = Book.objects.create(**self.book_data)

    def test_get_books_list(self):
        response = self.client.get(self.books_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_books_list_empty(self):
        Book.objects.all().delete()
        response = self.client.get(self.books_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
