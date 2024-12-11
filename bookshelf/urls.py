from django.urls import path
from . import views

urlpatterns = [
    path ("", views.index, name="index"),
    path ("<int:Page_Number>/", views.offset_index, name="more_index")
]
