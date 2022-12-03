from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import todo
from .forms import create_todo
# Create your views here.
def home_view(request):
    context={"todos":todo.objects.all()}
    return render(request,"notes/home.html",context)

def about_view(request):
    return render(request,"notes/about.html")

def todo_create_view(request):
    if request.method=="POST":
        form=create_todo(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form=create_todo()
    context={"form":form}
    return render(request,"notes/create_todo.html",{"form":form})

def update_todo(request,pk):
    todos=todo.objects.get(id=pk)
    
    form=create_todo(instance=todos)
    if request.method=="POST":
        form=create_todo(request.POST,instance=todos)
        if form.is_valid():
            form.save()
            return redirect("/")
    context={"form":form}
       
    return render(request,"notes/update_todo.html",context)

def delete_todo(request,pk):
    item=todo.objects.get(id=pk)
    if request.method=="POST":
        item.delete()
        return redirect("/")
    context={"item":item}
    return render(request,"notes/delete_todo.html",context)

