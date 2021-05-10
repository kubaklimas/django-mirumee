from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView,CreateAPIView
from rest_framework.views import APIView
from books.models import Book, Opinion
from books.api.serializers import BookSerializer, OpinionSerializer

from rest_framework.viewsets import GenericViewSet
from rest_framework.filters import SearchFilter

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    search_fields = [
        "title",
    ]
    filter_backends = [SearchFilter,]

class OpinionViewSet(ModelViewSet):
    queryset = Opinion.objects.all()
    serializer_class = OpinionSerializer