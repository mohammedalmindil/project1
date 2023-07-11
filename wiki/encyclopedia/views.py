from django.http import HttpResponse
from django.shortcuts import render
from encyclopedia import util
from . import util
from markdown2 import Markdown

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def CreatePage(request):
    if request.method=="POST":
        form= request.POST
        title= form["title"]
        content= form["content"]
        util.save_entry(title,content)
        return render (request, "encyclopedia/randompage.html")
    else:     
        return render(request,"encyclopedia/createPage.html")

def RandomPage(request):
    return render(request,"encyclopedia/randompage.html")
def EntryPage(request):
    if request.method=="GET":
        form= request.POST
        title=form["title"]
        listE=util.list_entries
        if title in listE:
            markdown=Markdown()
            markdown.convert(title)
