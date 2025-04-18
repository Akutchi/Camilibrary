import os

from django.shortcuts import render, redirect
from django.http import Http404, JsonResponse

from .models import Book, Tag

from .ORM_utils import (
    Extract_Authors,
    Extract_Tags,
    Get_Books_With_Authors,
    Get_Pagination,
    Filter_Books_With,
)

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
Books_On_Page = 36
Pagination_Number = 5

#  I litterally prefetched the databse in memory because, in my mind, the
#  function Filter_Books_With in offset_index will be called numerous times :
#  each time we access camilibrary.fr/X/(Filters).
#
#  This is potentially much more than book_view (that also use this prefetch)
#  and thus I find it inefficient to call it everytime.
#
# TODO : create a cache system.

OverAll = {
    "prefetched": Book.objects.prefetch_related("Tags")
    .prefetch_related("Authors")
    .all(),
    "page_books": [],
    "recent": Book.objects.order_by("-Added").order_by("-id")[:4].values(),
    "tags": Tag.objects.order_by("TagName").values(),
}

Get_Books_With_Authors(OverAll, Cut_Author_List_With="etc.")
OverAll["page_books"].sort(key=lambda item: item["authors"][0]["order_by"])


def index(req):
    return redirect("more_index", Page_Number=1)


def Format_Parameters_For_Template(Tag_List):
    if Tag_List is None:
        return "?filter="

    Tag_List = [t.replace(" ", "-") for t in Tag_List.split(" ")]
    query = "?filter=" + "+".join(Tag_List)

    return query


def offset_index(req, Page_Number):
    Tag_List = req.GET.get("filter")
    Books = Filter_Books_With(Tag_List, OverAll)

    if Books["page_books"] == []:
        return render(
            req,
            "index.html",
            {
                "recent": OverAll["recent"],
                "page_books": [],
                "tags": OverAll["tags"],
                "pagination": {
                    "current": -1,
                    "query": Format_Parameters_For_Template(Tag_List),
                },
            },
        )

    Books_Count = len(Books["page_books"])
    Pages_Count = Books_Count / Books_On_Page

    if Pages_Count.is_integer():
        Pages_Count = int(Pages_Count)
    else:
        Pages_Count = int(Pages_Count) + 1

    if Page_Number <= 0 or Page_Number > Pages_Count:
        raise Http404("bookshelf not found")

    Offset_Start = (Page_Number - 1) * Books_On_Page
    Offset_End = Page_Number * Books_On_Page
    Pagination = Get_Pagination(Page_Number, Pages_Count)

    Info = {
        "recent": OverAll["recent"],
        "page_books": Books["page_books"][Offset_Start:Offset_End],
        "tags": OverAll["tags"],
        "pagination": {
            "current": Page_Number,
            "page_list": [p for p in Pagination],
            "first_ellipses": Page_Number >= 3,
            "last_ellipses": Page_Number <= Pages_Count - 3,
            "query": Format_Parameters_For_Template(Tag_List),
        },
    }

    return render(req, "index.html", Info)


def search_view(req):
    placeholder = {
        "title": Book.objects.get(id=1).Title + "rogljegojetgemtgje",
        "image": Book.objects.get(id=1).Image.name,
        "id": "1",
    }
    return JsonResponse({"info": [placeholder, placeholder]})


def book_view(req, Book_Number):
    Books_Count = Book.objects.count()
    if Book_Number < 1 or Book_Number - 1 > Books_Count:
        raise Http404("book not found")

    Book_Obj = (
        Book.objects.prefetch_related("Tags")
        .prefetch_related("Authors")
        .get(pk=Book_Number)
    )
    Authors = Extract_Authors(Book_Obj)
    Tags = Extract_Tags(Book_Obj)

    Info = {"book_info": Book_Obj, "Authors": Authors, "Tags": Tags}

    PATH = (
        BASE_PATH + "/static/txt/" + Book_Obj.Image.name.split(".")[0].lower() + ".html"
    )

    if not os.path.exists(PATH):
        print("File does not exist")
        Info["CommentaryText"] = ""

    else:
        templ = open(PATH, "r").read()
        Info["CommentaryText"] = templ

    return render(req, "book.html", Info)


def graph_rendering(req):
    return render(req, "graph.html")


def about(req):
    PATH = BASE_PATH + "/static/txt/Liste_yuri.txt"

    if not os.path.exists(PATH):
        print("File does not exist")
        return render(req, "about.html", {"yuri_list": "File not found, rip"})

    yuri_list = open(PATH, "r").read()
    return render(req, "about.html", {"yuri_list": yuri_list})
