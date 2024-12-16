from django.shortcuts import render, redirect
from django.http import Http404

from .models import Book, Tag

from .ORM_utils import Get_Authors_For, Get_Tags_For, Get_Books_With_Authors, Get_Pagination, Filter_For_Tags

Books_On_Page = 21
Pagination_Number = 5

OverAll = {
            "page_books": [],
            "recent": Book.objects.order_by ("-Added")[:4].values(),
            "tags": Tag.objects.order_by ("TagName").values(),
        }

Get_Books_With_Authors (OverAll)
OverAll ["page_books"].sort (key=lambda item: item ["authors"][0]["order_by"])


def index (req):
    return redirect ("more_index", Page_Number=1)


def Format_Parameters_For_Template (Tag_List):

    if Tag_List == None:
        return "?filter="

    Tag_List = [t.replace("_", " ") for t in Tag_List.split(" ")]
    query = "?filter="+"+".join (Tag_List)+"+"

    return query


def offset_index (req, Page_Number):

    Tag_List = req.GET.get ("filter")
    Books = Filter_For_Tags (Tag_List, OverAll)

    if Books ["page_books"] == []:
        return render (req, "index.html", {
                                        "recent": OverAll ["recent"],
                                        "page_books": [],
                                        "tags": OverAll ["tags"],
                                        "pagination": {
                                                        "current": -1,
                                                        "query": Format_Parameters_For_Template (Tag_List)

                                        }
                                    })

    Books_Count = len(Books ["page_books"])
    Pages_Count = Books_Count/Books_On_Page

    if Pages_Count.is_integer():
        Pages_Count = int(Pages_Count)
    else:
        Pages_Count = int(Pages_Count)+1

    if (Page_Number <= 0 or Page_Number > Pages_Count):
        raise Http404 ("bookshelf not found")

    Offset_Start = (Page_Number-1)*Books_On_Page
    Offset_End = Page_Number*Books_On_Page
    Pagination = Get_Pagination (Page_Number, Pages_Count)


    Info = {
                "recent": OverAll ["recent"],
                "page_books": Books ["page_books"][Offset_Start:Offset_End],
                "tags": OverAll ["tags"],
                 "pagination": {
                                "current": Page_Number,
                                "page_list": [p for p in Pagination],
                                "first_ellipses": Page_Number >= 3,
                                "last_ellipses": Page_Number <= Pages_Count-3,
                                "query": Format_Parameters_For_Template (Tag_List)
                                }
            }

    return render (req, "index.html", Info)


def book_view (req, Book_Number):

    Books_Count = Book.objects.count()

    if (Book_Number < 1 or Book_Number > Books_Count):
        raise Http404 ("book not found")

    Book_Obj = Book.objects.get (pk=Book_Number)
    Authors = Get_Authors_For (Book_Number)
    Tags = Get_Tags_For (Book_Number)

    Info = {"book_info": Book_Obj, "Authors": Authors, "Tags": Tags}

    return render (req, "book.html", Info)