from django.contrib import admin
from .models import Book, Author, Tag, Book_Author_Link, Book_Tag_Link

admin.site.register (Book)
admin.site.register (Tag)
admin.site.register (Author)
admin.site.register (Book_Author_Link)
admin.site.register (Book_Tag_Link)