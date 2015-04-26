import json

from django.http import HttpResponse
from django.views.generic import View

from .models import Book


class BookListView(View):
    def get(self, request, *args, **kwargs):
        result = [o.to_dict() for o in Book.objects.all()]
        return HttpResponse(json.dumps(result))
