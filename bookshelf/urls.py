from django.urls import path
from . import views

urlpatterns = [
    path ("", views.index, name="index"),
    path ("<int:Page_Number>", views.offset_index, name="more_index"),
    path ("search", views.search_view, name="search"),
    path ("book/<int:Book_Number>", views.book_view, name="book_page"),
    path ("about", views.about, name="about"),
]
