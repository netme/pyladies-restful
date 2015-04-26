import json

from django.core.urlresolvers import reverse
from django.test import TestCase

from .models import Book


class BookGetListTest(TestCase):

    def test_returns_the_list(self):
        books = [
            {'name': 'Django Book', 'price': '29.90'},
            {'name': 'Python Cookbook', 'price': '39.90'}
        ]
        book_objects = []
        for book in books:
            book_object = Book(**book)
            book_object.save()
            book_objects.append(book_object)

        response = self.client.get(reverse('books'))

        self.assertEqual(response.status_code, 200)
        result = json.loads(response.content)
        self.assertEqual(result, books)


class BookGetInstanceTest(TestCase):
    def test_wrong_id(self):
        response = self.client.get('/books/9999999999/')
        self.assertEqual(response.status_code, 404)
