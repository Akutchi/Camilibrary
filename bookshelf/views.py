from django.shortcuts import render
from django.http import Http404

from .models import Book, Tag

from .ORM_utils import Get_Authors_For, Get_Tags_For, Get_Books_With_Authors

Books_On_Page = 21
Books_Count = Book.objects.count()
Pages_Count = int(Books_Count/Books_On_Page)

OverAll = {
            "page_books": [],
            "recent": Book.objects.order_by ("-Added")[:4].values(),
            "tags": Tag.objects.order_by ("TagName").values(),
        }

Get_Books_With_Authors (OverAll)
OverAll ["page_books"].sort (key=lambda item: item ["authors"][0]["order_by"])

def index (req):

    Unbound_Pagination = [p for p in range (1, 4)]
    Bounded_Pagination = filter(lambda i: False if i < 1 else True,
                                filter (lambda i: False if i > Pages_Count else True,
                                        Unbound_Pagination))

    Info = {
                "recent": OverAll ["recent"],
                "page_books": OverAll ["page_books"][0:Books_On_Page],
                "tags": OverAll ["tags"],
                "pagination": {"current": 1, "page_list": [p for p in Bounded_Pagination]}
            }

    return render (req, "index.html", Info)


def offset_index (req, Page_Number):

    Begin_Number = (Page_Number-1)*Books_On_Page
    End_Number = Page_Number*Books_On_Page

    if (Begin_Number <= 0 or Begin_Number > Books_Count or End_Number > Books_Count):
        raise Http404 ("bookshelf not found")

    Unbound_Pagination = [p for p in range (Page_Number-3, Page_Number+3)]
    Bounded_Pagination = filter(lambda i: False if i < 1 else True,
                                filter (lambda i: False if i > Pages_Count+1 else True,
                                        Unbound_Pagination))

    Info = {
                "recent": OverAll ["recent"],
                "page_books": OverAll ["page_books"][Begin_Number:End_Number],
                "tags": OverAll ["tags"],
                "pagination": {"current": Page_Number, "page_list": [p for p in Bounded_Pagination]}
            }

    return render (req, "index.html", Info)


def book_view (req, Book_Number):

    if (Book_Number < 1 or Book_Number > Books_Count):
        raise Http404 ("book not found")

    Book_Obj = Book.objects.get (pk=Book_Number)
    Authors = Get_Authors_For (Book_Number)
    Tags = Get_Tags_For (Book_Number)

    Info = {"book_info": Book_Obj, "Authors": Authors, "Tags": Tags}

    return render (req, "book.html", Info)