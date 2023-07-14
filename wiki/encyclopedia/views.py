from django.http import HttpResponse
from django.shortcuts import render
from encyclopedia import util
from . import util
import markdown2

def Duplication(entry):
    if util.get_entry(entry) is not None:
        return True
    else:
        return False
def convert(entry):
       title=util.get_entry(entry)
       if title==None:
            return None
       else:
          return markdown2.markdown(title) 

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
            entry=convert(title)
            return render(request,"encyclopedia/entrypage.html",{
                "Title":title,
                "content":entry
             })
    else:     
        return render(request,"encyclopedia/createPage.html")
    

def RandomPage(request):
    return render(request,"encyclopedia/randompage.html")




def ResultPage(request):
    return render(request,"encyclopedia/result.html")

def EntryPage(request,name):
    entry=convert(name)
    if entry is not None:
        return render(request,"encyclopedia/entrypage.html",{
         "Title":name,
         "content":entry
     }) 
    else:
     return render(request,"encyclopedia/result.html",{
                "Result": "Error" ,
                "descrption":"entry doesn't exists"
            })


def SearchPage(request):
    if request.method=="POST":
        listEntry=util.list_entries()
        listResult=[]
        form= request.POST
        title=form["q"]
        entry=convert(title)
        if entry is not None:
            return render(request,"encyclopedia/entrypage.html",{
                "Title":title,
                "content":entry
             })
        else:
            for i in listEntry:
                if title.lower() in i.lower():
                    listResult.append(i)
            if len(listResult)== 0:
                return render(request,"encyclopedia/result.html",{
                "Result": "Error" ,
                "descrption":"entry doesn't exists"
            })
            else:
             return render (request, "encyclopedia/searchpage.html",{
                "list":listResult
             })
            

def EditPage(request):
    if request.method=="POST":
        form= request.POST
        title= form["titleE"]
        entry=util.get_entry(title)
        return render(request,"encyclopedia/editpage.html",{
         "Title":title,
         "content":entry
             })
def SaveEdit(request):
    if request.method =="POST":
        form= request.POST
        title= form["title"]
        content= form["content"]
        util.save_entry(title,content)
        entry=convert(title)
        return render(request,"encyclopedia/entrypage.html",{
                "Title":title,
                "content":entry
             })