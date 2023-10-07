from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"shop/index.html",{}) 

def fixed(request):
    return render(request,"shop/fixed.html",{})

def Nonfixed(request):
    return render(request,"shop/Nonfixed.html",{})

def Statement(request):
    return render(request,"shop/Statement.html",{})

def help(request):
    return render(request,"shop/help.html",{})

def about(request):
    return render(request,"shop/about.html",{})
