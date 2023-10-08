from django.db import models

class FixedAmount(models.Model):
    date = models.DateField(default="")
    type = models.CharField(max_length=50,default="")
    shop_name = models.CharField(max_length=200,default="")
    invoice_no = models.CharField(max_length=20,default="") 
    item_name = models.CharField(max_length=200,default="")
    qty = models.IntegerField(default="")
    price = models.IntegerField(default="")

class NonFixedAmount(models.Model):
    date = models.DateField(default="")
    type = models.CharField(max_length=50,default="")
    shop_name = models.CharField(max_length=200,default="")
    invoice_no = models.CharField(max_length=40,default="")
    item_name = models.CharField(max_length=200,default="")
    qty = models.IntegerField(default="")
    price = models.IntegerField(default="")