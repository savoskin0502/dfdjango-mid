from django.contrib import admin
from .models import Book, Journal


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'created_at',
                    'num_pages', 'genre']
    ordering = ['-price']
    search_fields = ['name__contains']
    list_filter = ['genre']


admin.site.register(Journal)
