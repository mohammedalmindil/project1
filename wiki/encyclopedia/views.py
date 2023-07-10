from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def CreatePage(request):
    return render(request,"encyclopedia/createPage.html")

def RandomPage(request):
    return render(request,"encyclopedia/randompage.html")