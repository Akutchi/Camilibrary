from django.shortcuts import render

from .models import Book, Tag

from .ORM_utils import Get_Authors_For, Get_Tags_For, Get_Books_With_Authors

Books_On_Page = 21
OverAll = {
            "page_books": [],
            "recent": Book.objects.order_by ("-Added")[0:4].values(),
            "tags": Tag.objects.order_by ("TagName").values()
        }

Get_Books_With_Authors (OverAll)
OverAll ["page_books"].sort (key=lambda item: item ["authors"][0]["order_by"])


def index (req):

    Info = {
                "recent": OverAll ["recent"],
                "page_books": OverAll ["page_books"][0:Books_On_Page],
                "tags": OverAll ["tags"]
            }

    return render (req, "index.html", Info)


def offset_index (req, Page_Number):

    Books_Count = Book.objects.count()
    Begin_Number = (Page_Number-1)*Books_On_Page
    End_Number = Page_Number*Books_On_Page

    if Begin_Number <= 0:
        Begin_Number = 0
        End_Number = Books_On_Page

    elif Begin_Number > Books_Count:
        Begin_Number = Books_Count-(Books_Count%Books_On_Page)
        End_Number = Books_Count

    elif End_Number > Books_Count:
        End_Number = Books_Count

    Info = {
                "recent": OverAll ["recent"],
                "page_books": OverAll ["page_books"][Begin_Number:End_Number],
                "tags": OverAll ["tags"]
            }

    return render (req, "index.html", Info)


def book_view (req, Book_Number):

    Book_Obj = Book.objects.get (pk=Book_Number)
    Authors = Get_Authors_For (Book_Number)
    Tags = Get_Tags_For (Book_Number)

    Info = {"book_info": Book_Obj, "Authors": Authors, "Tags": Tags}

    return render (req, "book.html", Info)