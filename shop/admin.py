from django.contrib import admin
from .models import FixedAmount,NonFixedAmount

# Register your models here.
admin.site.register(FixedAmount)
admin.site.register(NonFixedAmount)