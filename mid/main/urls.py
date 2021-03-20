from django.urls import path, include
from rest_framework import routers

from .views import BooksViewSet, JournalsViewSet

# router = routers.SimpleRouter()
# router.register(r'', TodoListViewSet, basename='main')
# router.register(r'', TodoViewSet, basename='main')

urlpatterns = [
    path('books/', BooksViewSet.as_view({
        'get': 'get_books',
        'post': 'create'
    })),
    path('journals/', JournalsViewSet.as_view({
        'get': 'get_journals'
    }))
]
# urlpatterns += router.urls
# print('routes', router.urls, urlpatterns)
