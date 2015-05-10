import json
from decimal import Decimal

from django.core.urlresolvers import reverse
from django.test import TestCase

from .models import Book


class BookGetListTest(TestCase):

    def test_returns_the_list(self):
        books = [
            {'name': 'Django Book', 'price': Decimal('29.90')},
            {'name': 'Python Cookbook', 'price': Decimal('39.90')}
        ]
        book_objects = []
        for book in books:
            book_object = Book(**book)
            book_object.save()
            book_objects.append(book_object)

        expected_result = [b.to_dict() for b in book_objects]

        response = self.client.get(reverse('books'))

        self.assertEqual(response.status_code, 200)
        result = json.loads(response.content)
        self.assertEqual(result, expected_result)


class BookGetInstanceTest(TestCase):

    def test_wrong_id(self):
        response = self.client.get('/books/9999999999/')
        self.assertEqual(response.status_code, 404)

    def test_returns_the_details(self):
        book = Book(name='Django Book', price=Decimal('29.90'))
        book.save()

        response = self.client.get(reverse('book', kwargs={'id_': book.id}))

        self.assertEqual(response.status_code, 200)
        result = json.loads(response.content)
        self.assertEqual(result['name'], book.name)
        self.assertEqual(result['price'], '{:2f}'.format(book.price))
        self.assertEqual(result['url'], book.url)


class BookModelTest(TestCase):

    def test_url_property_of_saved_object(self):
        book = Book(name='Django Book', price=Decimal('29.90'))
        book.save()
        self.assertEqual(book.url, '/books/{}/'.format(book.id))

    def test_url_property_of_non_saved_object(self):
        book = Book(name='Django Book', price=Decimal('29.90'))
        self.assertIsNone(book.url)
