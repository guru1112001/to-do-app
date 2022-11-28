from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import register_form,login_form
from django.contrib import messages
# Create your views here.

def login_view(request):
    if request.method=="POST":
        form=register_form(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request,username=cd["username"],password=cd["password"])

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse("you have been login")
                else:
                    return HttpResponse("disable account")
            else:
                return HttpResponse("invalid loign")
    else:
        form=login_form
    return render(request,"user/login.html",{"form":form})

def register_view(request):
    form=register_form()
    if request.method=="POST":
        form=register_form(request.POST)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse("your account has been register ")
    
    form=register_form()
    return render(request,"user/register.html",{"form":form})
