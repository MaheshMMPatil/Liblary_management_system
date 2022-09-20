from django.urls import path
from .import views

urlpatterns = [
    path('b1/',views.AddBook.as_view(),name="addurl"),
    path('b2/',views.StudentView.as_view(),name="showbookurl"),
    path('b3/<int:id>/',views.BookUpdate.as_view(),name="updatebookurl"),
    path('b4/<int:id>/',views.DeleteBook.as_view(),name="deletebookurl")
]