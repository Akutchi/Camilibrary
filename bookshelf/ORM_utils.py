from .models import Book, Book_Author_Link, Book_Tag_Link, Author, Tag

import random as rnd

def Get_Authors_For (Book_Primary_Key):

    Authors_Linked = Book_Author_Link.objects.filter (Book_Key=Book_Primary_Key).values()
    Authors_List = []
    for A in Authors_Linked:

        One_Author = Author.objects.get (id=A ["Author_Key_id"])

        Authors_List.append ({"order_by": One_Author.Surname.lower(),
                                "value": One_Author.Name + " " +
                                        One_Author.Surname + ", "
                            })

    Authors_List.sort (key=lambda item: item ["order_by"])
    Authors_List[-1]["value"] = Authors_List [-1]["value"][0:-2]  #  delete last comma

    return Authors_List

def Get_Tags_For (Book_Primary_Key):

    max_val = 10
    Angles = [alpha for alpha in range (-max_val, max_val, 2)]

    Tag_Linked = Book_Tag_Link.objects.filter (Book_Key=Book_Primary_Key).values()
    Tag_List = []

    for T in Tag_Linked:

        One_Tag = Tag.objects.get (id=T ["Tag_Key_id"])
        Tag_List.append ({"value": One_Tag.TagName, "style" : {"TagRotation": rnd.choice (Angles)}})

    return Tag_List

def Get_Books_With_Authors (General_Object):

    for B in Book.objects.all():

        Authors_List = Get_Authors_For (B.pk)
        General_Object["page_books"].append ({"info": B, "authors": Authors_List})

    return General_Object

def Filter_Book (Book_Obj, filters):

    Result = Book_Obj.filter (Tags__TagName=filters [0])
    for F in filters [1:]:

        Result = Result & Book_Obj.filter (Tags__TagName=F)

    return Result

def Filter_For_Tags (Tags, Every_Books):

    if Tags == None:
        return Every_Books

    filters_tag = [t.replace("_", " ") for t in Tags.split(" ")]
    # Tags in the form of ['XXX YYY Z_Z_ZZ']

    General_Object = {"page_books": []}
    Filtered_Books = Filter_Book (Book.objects, filters_tag)

    for B in Filtered_Books:

        Authors_List = Get_Authors_For (B.pk)
        General_Object["page_books"].append ({"info": B, "authors": Authors_List})

    return General_Object

def Get_Pagination (Page_Number, Pages_Count):

    if Pages_Count <= 5:
        return [p for p in range (1, Pages_Count+1)]

    if Page_Number <= 3:
        return [1, 2, 3, 4, Pages_Count]

    if Page_Number >= Pages_Count-3:
        return [1, Pages_Count-3, Pages_Count-2, Pages_Count-1, Pages_Count]

    overflow_negative = lambda i: False if i < 1 else True
    overflow_max = lambda i: False if i > Pages_Count else True

    Unbound_Pagination = list(set((1, *(p for p in range (Page_Number-3, Page_Number+3)), Pages_Count)))
    Bounded_Pagination = filter(overflow_negative,
                                filter (overflow_max,
                                        Unbound_Pagination))

    return Bounded_Pagination