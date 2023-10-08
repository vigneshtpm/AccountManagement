from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import FixedAmount, NonFixedAmount

# Create your views here.
def index(request):
    return render(request,"shop/index.html",{}) 

def fixed(request):
    return render(request,"shop/fixed.html",{})

def insertfixed(request):
    date1=request.POST['billdate1'];
    shop_name1=request.POST['shopname1'];
    invoice_no1=request.POST['invoiceno1'];
    item_name1=request.POST['itemname1'];
    qty1=request.POST['qty1'];
    price1=request.POST['amount1'];
    us=FixedAmount(date=date1,type="fixed expense",shop_name=shop_name1,invoice_no=invoice_no1,item_name=item_name1,qty=qty1,price=price1);
    us.save();
    return render (request,"shop/fixed.html",{})

def insertnonfixed(request):
    date2=request.POST['billdate2'];
    shop_name2=request.POST['shopname2'];
    invoice_no2=request.POST['invoiceno2'];
    item_name2=request.POST['itemname2'];
    qty2=request.POST['qty2'];
    price2=request.POST['amount2'];
    us=NonFixedAmount(date=date2,type="non_fixed expense",shop_name=shop_name2,invoice_no=invoice_no2,item_name=item_name2,qty=qty2,price=price2);
    us.save();
    return render (request,"shop/Nonfixed.html",{})

def Nonfixed(request):
    return render(request,"shop/Nonfixed.html",{})

def Statement(request):
    return render(request,"shop/Statement.html",{})

def help(request):
    return render(request,"shop/help.html",{})

def about(request):
    return render(request,"shop/about.html",{})
