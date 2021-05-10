from rest_framework import serializers
from books.models import Book, Opinion

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Book
        fields = ['isbn','title','author','genre']

class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Opinion
        fields = ['isbn','mark','comment']

