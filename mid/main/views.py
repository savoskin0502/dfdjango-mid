from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from .models import Book, Journal
from .serializers import BookSerializer, JournalSerializer


class BooksViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Book.objects.all()

    def get_books(self, request):
        serializer = BookSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def create(self, request, **kwargs):
        if request.user.role == 'SuperAdmin':
            book = Book(name=request.data['name'],
                        price=request.data['price'],
                        description=request.data.get('description', ''),
                        num_pages=request.data.get('num_pages', 0),
                        genre=request.data.get('genre', 'Not Defined'))
            book.save()
        return Response(data=request.data)


class JournalsViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Journal.objects.all()

    def get_journals(self, request):
        serializer = JournalSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def create(self, request, **kwargs):
        journal = Journal(name=request.data['name'],
                          price=request.data['price'],
                          description=request.data.get('description', ''),
                          type=request.data.get('type', 'Food'))
        journal.save()
        return Response(data=request.data)
