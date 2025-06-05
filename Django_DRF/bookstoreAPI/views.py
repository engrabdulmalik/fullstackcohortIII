from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import generics
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class BookList(generics.ListCreateAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    ordering_fields = ['id']
    search_fields = ['title', 'author']
    filterset_fields = ['title']
    

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
      # Ensure only authenticated users can access this view
class RatingsView(generics.ListCreateAPIView):
    queryset = models.Rating.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.RatingSerializer

    # Automatically set the user to the current authenticated user