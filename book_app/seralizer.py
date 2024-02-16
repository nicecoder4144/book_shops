from .models import Category,Author,Book

from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    category_status = serializers.BooleanField(source='category.status')
    class Meta:
        model = Book
        fields = ('id','name','category_status','category_name','author','description','photo','isbn','file','audio','dounloads_count')



class CategorySerilaizer(serializers.ModelSerializer):
    book_category = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('name','id','created_at','book_category')

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('full_name','id','status')

