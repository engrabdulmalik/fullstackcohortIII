from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import generics

# Create your views here.

class BookList(generics.ListCreateAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
