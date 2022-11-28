from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import todo
# Create your views here.
def home_view(request):
    context={"todos":todo.objects.all()}
    return render(request,"notes/home.html",context)


