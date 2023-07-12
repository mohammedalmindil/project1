from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("CreatePage", views.CreatePage,name="createpage"),
    path("RandomPage", views.RandomPage,name="randompage"),
    path("ResultPage",views.ResultPage, name="result"),
    path("wiki/<str:name>",views.EntryPage ,name="entrypage")
]
