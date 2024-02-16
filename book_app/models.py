from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Categoriya nomi')

    status = models.BooleanField(default=True,verbose_name='Holati')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'
        

    def __str__(self):
        return self.name


class Author(models.Model):
    full_name = models.CharField(max_length=40, verbose_name='Muallifi')

    status = models.BooleanField(default=True, verbose_name='Holati')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Muallif'
        verbose_name_plural = 'Mualliflar'
        

    def __str__(self):
        return self.full_name
        

class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Kategoriyasi',related_name='book_category')
    author = models.ForeignKey(Author,on_delete=models.CASCADE, verbose_name='Muallifi')
    name = models.CharField(max_length=40)
    description = models.TextField(verbose_name="ta'rif")
    photo = models.ImageField(upload_to='book_photo/%Y/%m/%d/', verbose_name='Rasmi')
    isbn = models.PositiveIntegerField(verbose_name='Kitobning id raqami')
    file = models.FileField(upload_to='book_file/%Y/%m/%d/', verbose_name='File')
    audio = models.FileField(upload_to='book_audio/%Y/%m/%d/', verbose_name='Audiosi')
    dounloads_count = models.PositiveIntegerField(default=0, verbose_name='Yuklab olishlar soni')

    status = models.BooleanField(default=True, verbose_name='Holati')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Kitob'
        verbose_name_plural = 'Kitoblar'
        
    def __str__(self):
        return self.name











# pip install django #djangoni o'rnatish
# django-admin startproject config . #loyiha boshlash
# python manage.py myapp


