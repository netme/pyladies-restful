import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import View

from .models import Book


class BookListView(View):
    def get(self, request, *args, **kwargs):
        result = [o.to_dict() for o in Book.objects.all()]
        return HttpResponse(json.dumps(result))


class BookView(View):
    def get(self, request, id_, *args, **kwargs):
        book = get_object_or_404(Book, pk=id_)
        json_data = json.dumps(book.to_dict())
        return HttpResponse(json_data)
