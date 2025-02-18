from django.contrib import admin
from django.db.models import F

from .models import Book, Author, Tag, Book_Author_Link, Book_Tag_Link

@admin.register (Book)
class MyModelAdmin(admin.ModelAdmin):
    ordering = [F('Title').asc(nulls_last=True)]

@admin.register (Author)
class MyModelAdmin(admin.ModelAdmin):
    ordering = [F('Surname').asc(nulls_last=True)]

@admin.register (Tag)
class MyModelAdmin(admin.ModelAdmin):
    ordering = [F('TagName').asc(nulls_last=True)]

@admin.register (Book_Author_Link)
class MyModelAdmin(admin.ModelAdmin):
    ordering = [F('Book_Key')]

@admin.register (Book_Tag_Link)
class MyModelAdmin(admin.ModelAdmin):
    ordering = [F('Book_Key')]