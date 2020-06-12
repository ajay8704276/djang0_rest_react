from django.contrib import admin

# Register your models here.
from dummyapp.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    #fields = ['title', 'description']
    list_display = ['title', 'description','price']
