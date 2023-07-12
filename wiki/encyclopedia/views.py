from django.http import HttpResponse
from django.shortcuts import render
from encyclopedia import util
from . import util
import markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def CreatePage(request):
    if request.method=="POST":
        form= request.POST
        title= form["title"]
        content= form["content"]
        if Duplication(title)== True:
            return render(request,"encyclopedia/result.html",{
                "Result": "Error" ,
                "descrption":"entry already exists"
            })
        else:
            util.save_entry(title,content)
            return render(request,"encyclopedia/result.html",{
                "Result": "Success" ,
                "descrption":"entry successfully added"
            })
    else:     
        return render(request,"encyclopedia/createPage.html")
    

def RandomPage(request):
    return render(request,"encyclopedia/randompage.html")


def Duplication(entry):
    if util.get_entry(entry) is not None:
        return True
    else:
        return False
    

def ResultPage(request):
    return render(request,"encyclopedia/result.html")

def EntryPage(request,name):
    content=Convert(name)
    if content==None:
        return render(request,"encyclopedia/result.html",{
                "Result": "Error" ,
                "descrption":"entry doesn't exists"
            })
    else:
     return render(request,"encyclopedia/entrypage.html",{
         "title":name,
         "content":content
     })
def Convert(entry):
    title=util.get_entry(entry)
    markdowner = markdown.Markdown()
    if title==None:
        return None
    else:
       return  markdowner.convert(entry)
        