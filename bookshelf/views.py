from django.shortcuts import render
from django.http import Http404

from .models import Book, Tag

from .ORM_utils import Get_Authors_For, Get_Tags_For, Get_Books_With_Authors, Get_Pagination

Books_On_Page = 21
Books_Count = Book.objects.count()
Pages_Count = Books_Count/Books_On_Page
Pagination_Number = 5

if Pages_Count.is_integer():
    Pages_Count = int(Pages_Count)
else:
    Pages_Count = int(Pages_Count)+1

OverAll = {
            "page_books": [],
            "recent": Book.objects.order_by ("-Added")[:4].values(),
            "tags": Tag.objects.order_by ("TagName").values(),
        }

Get_Books_With_Authors (OverAll)
OverAll ["page_books"].sort (key=lambda item: item ["authors"][0]["order_by"])

def index (req):

    Unbound_Pagination = list(set((1, *(p for p in range (2, Pagination_Number)), Pages_Count)))
    Bounded_Pagination = filter(lambda i: False if i < 1 else True,
                                filter (lambda i: False if i > Pages_Count else True,
                                        Unbound_Pagination))

    Info = {
                "recent": OverAll ["recent"],
                "page_books": OverAll ["page_books"][0:Books_On_Page],
                "tags": OverAll ["tags"],
                "pagination": {
                                "current": 1,
                                "page_list": [p for p in Bounded_Pagination],
                                "first_ellipses": True,
                                "last_ellipses": True # Pages_Count > Pagination_Number
                                }
            }

    return render (req, "index.html", Info)


def offset_index (req, Page_Number):

    if (Page_Number <= 0 or Page_Number > Pages_Count):
        raise Http404 ("bookshelf not found")

    Offset_Start = (Page_Number-1)*Books_On_Page
    Offset_End = Page_Number*Books_On_Page

    Pagination = Get_Pagination (Page_Number, Pages_Count)

    Info = {
                "recent": OverAll ["recent"],
                "page_books": OverAll ["page_books"][Offset_Start:Offset_End],
                "tags": OverAll ["tags"],
                 "pagination": {
                                "current": Page_Number,
                                "page_list": [p for p in Pagination],
                                "first_ellipses": Page_Number >= 3,
                                "last_ellipses": Page_Number <= Pages_Count-3
                                }
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