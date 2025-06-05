from rest_framework import serializers
from . import models
from .models import Rating
from django.contrib.auth.models import User
from rest_framework.validators import UniqueTogetherValidator

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ['id', 'title', 'author', 'price']  # Include all fields you want to serialize
         # Make 'id' read-only if you don't want it to be set on creation

class RatingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField( 
    queryset=User.objects.all(), 
    default=serializers.CurrentUserDefault() 
    )
    class Meta:
        model = Rating
        fields = ['user', 'book', 'rating']

        validators = [
            UniqueTogetherValidator(
                queryset=Rating.objects.all(),
                fields=['user', 'book']
            )
        ]

        extra_kwargs = {
            'rating': {'min_value': 0, 'max_value':5},
        }# Include all fields you want to serialize
         # Make 'id' read-only if you don't want it to be set on creation