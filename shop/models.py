from django.db import models

class Fixed(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=200)
    invoice_no = models.CharField(max_length=20)
    qty = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)