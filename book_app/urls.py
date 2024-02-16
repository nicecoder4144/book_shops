
from .views import CategoryViewset,AuthorViewset,BookViewset
from django.urls import path,include
from rest_framework import routers

router = routers.DefaultRouter()

router.register('category',CategoryViewset,basename='category')
router.register('author',AuthorViewset,basename='author')
router.register('book',BookViewset,basename='book')

urlpatterns = [
    path('',include(router.urls))
]
