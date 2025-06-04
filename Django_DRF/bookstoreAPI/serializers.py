from rest_framework import serializers
from . import models

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ['id', 'title', 'author', 'price']  # Include all fields you want to serialize
         # Make 'id' read-only if you don't want it to be set on creation