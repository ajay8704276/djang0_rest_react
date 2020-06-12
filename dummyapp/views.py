from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


"""class Another(View):
    books = Book.objects.filter(is_published=True)
    output = ""
    for book in books:
        output += f"we have book with title {book.title} book in db having id {book.id}<br>"

    def get(self, request):
        return HttpResponse(self.output)


def first(request):
    books = Book.objects.all()
    return render(request, 'first_tempplate.html', {
        'book_data': books
    })"""
