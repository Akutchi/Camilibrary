from .models import Book

import random as rnd


def Authors_List_Too_Long(Author_List, ellipses=None):
    return ellipses is not None and len(Author_List) > 3


# this suppose you did a prefetch_related before
def Extract_Authors(Book, Cut_Author_List_With=None):
    Authors_List = []
    for Author in Book.Authors.all():
        Name = Author.Name if Author.Name != "." else ""
        Authors_List.append({
            "order_by": Author.Surname.lower(),
            "value": Name + " " + Author.Surname + ", ",
        })

    Authors_List.sort(key=lambda item: item["order_by"])

    if Authors_List == []:
        Authors_List = [{"order_by": "", "value": " "}]

    Authors_List[-1]["value"] = Authors_List[-1]["value"][0:-2]  #  delete last comma

    if Authors_List_Too_Long(Authors_List, ellipses=Cut_Author_List_With):
        Authors_List = Authors_List[0:3]
        Authors_List.append({"value": "etc."})

    return Authors_List


def Get_Books_With_Authors(General_Object, Cut_Author_List_With):
    Books = Book.objects.prefetch_related("Authors").all()
    for B in Books:
        Authors_List = Extract_Authors(B, Cut_Author_List_With)
        General_Object["page_books"].append({"info": B, "authors": Authors_List})

    return General_Object


# this suppose you did a prefetch_related before
def Extract_Tags(Book):
    max_val = 10
    Angles = [alpha for alpha in range(-max_val, max_val, 2)]

    Tag_List = []
    for T in Book.Tags.all():
        Tag_List.append({
            "value": T.TagName,
            "style": {"TagRotation": rnd.choice(Angles)},
        })

    return Tag_List


def Book_Has_Filters(Book_Tags, Filters):
    return len(list(set(Book_Tags) & set(Filters))) == len(Filters)


def Filter_Books_With(Tags, Every_Books):
    if Tags is None:
        return Every_Books

    Filters = [t.replace("-", " ") for t in Tags.split(" ")]
    # Tags in the form of ['XXX YYY Z-Z-ZZ']

    General_Object = {"page_books": []}
    for B in Every_Books["prefetched"]:
        Book_Tags = [T.TagName for T in B.Tags.all()]
        if Book_Has_Filters(Book_Tags, Filters):
            Authors_List = Extract_Authors(B, "etc.")
            General_Object["page_books"].append({"info": B, "authors": Authors_List})

    return General_Object


def Get_Pagination(Page_Number, Pages_Count):
    if Page_Number <= 3:
        return [1, 2, 3, 4, Pages_Count]

    if Page_Number > Pages_Count - 3:
        return [1, Pages_Count - 3, Pages_Count - 2, Pages_Count - 1, Pages_Count]

    overflow_negative = lambda i: False if i < 1 else True
    overflow_max = lambda i: False if i > Pages_Count else True

    Unbound_Pagination = list(
        set((1, *(p for p in range(Page_Number - 1, Page_Number + 2)), Pages_Count))
    )
    Bounded_Pagination = filter(
        overflow_negative, filter(overflow_max, Unbound_Pagination)
    )

    return Bounded_Pagination

