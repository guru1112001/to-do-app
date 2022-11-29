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
            return HttpResponse("todo is added")
    else:
        form=create_todo()
    context={"form":form}
    return render(request,"notes/create_todo.html",{"form":form})


