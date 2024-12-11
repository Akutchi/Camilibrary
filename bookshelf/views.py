from django.shortcuts import render
from django.http import JsonResponse

from .models import Book, Book_Author_Link, Author

def Get_Books (General_Object):

    for B in Book.objects.all():

        Authors_Linked = Book_Author_Link.objects.filter (Book_Key=B.pk)
        Authors_List = []

        for A in Authors_Linked.values():

            One_Author = Author.objects.get (id=A ["Author_Key_id"])

            Authors_List.append ({"order_by": One_Author.Surname.lower(),
                                  "value": One_Author.Name + " " +
                                           One_Author.Surname + ", "
                                })

        Authors_List.sort (key=lambda item: item ["order_by"])
        # delete last comma
        Authors_List[-1]["value"] = Authors_List [-1]["value"][0:-2]
        General_Object["context"].append ({"info": B, "authors": Authors_List})

    return General_Object

# creation of a new object because OverAll variable is passed by reference
def Serialize_Books (General_Object):

    New_Object = {"context": []}
    for Obj in General_Object:
        New_Dict = {"Title": Obj ["info"].Title, "Description": Obj ["info"].Description}
        New_Object ["context"].append ({"info": New_Dict, "authors": Obj ["authors"]})

    return New_Object

Books_On_Page = 21
OverAll = {"context": []}
Get_Books (OverAll)
OverAll ["context"].sort (key=lambda item: item ["authors"][0]["order_by"])

def index (req):

    return render (req, "index.html", {"context": OverAll ["context"][0:Books_On_Page]})

def offset_index (req, Page_Number):

    Books_Count = Book.objects.count()
    Begin_Number = (Page_Number-1)*Books_On_Page
    End_Number = Page_Number*Books_On_Page

    if Begin_Number > Books_Count:
        Begin_Number = Books_Count-(Books_Count%Books_On_Page)
        End_Number = Books_Count

    elif End_Number > Books_Count:
        End_Number = Books_Count

    return render (req, "index.html", {"context": OverAll ["context"][Begin_Number:End_Number]})

