from django.shortcuts import render
from .models import Book, Book_Author_Link, Author

def index (req):

    OverAll = {"context": []}

    for B in Book.objects.all():

        Authors_Linked = Book_Author_Link.objects.filter (Book_Key=B.pk)
        Authors_List = []

        for A in Authors_Linked.values():

            One_Author = Author.objects.get (id=A ["Author_Key_id"])

            Authors_List.append ({"order_by": One_Author.Surname.lower(),
                                  "value": One_Author.Name + " " +
                                           One_Author.Surname + ", "
                                })

        # delete last comma
        Authors_List[-1]["value"] = Authors_List [-1]["value"][0:-2]
        OverAll["context"].append ({"info": B, "authors": Authors_List})

    OverAll ["context"].sort (key=lambda item: item ["authors"][0]["order_by"])

    return render (req, "index.html", OverAll)