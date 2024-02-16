from django.shortcuts import render
from .models import Category,Author,Book
from .seralizer import CategorySerilaizer,AuthorSerializer,BookSerializer

from rest_framework import viewsets,serializers
from rest_framework.permissions import AllowAny,IsAuthenticated
# Create your views here.

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.filter(status=True)
    serializer_class = CategorySerilaizer
    permission_classes = [AllowAny]

class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.filter(status=True)
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]

class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.filter(status=True)
    serializer_class = BookSerializer
    permission_classes = [AllowAny]