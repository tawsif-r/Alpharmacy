from django.contrib import admin
from .models import *

model_arr = [Pharmacy_owner,Pharmacy,Medicine,Customer,Order,OrderItem,ShippingAddress]
for i in model_arr:
    admin.site.register(i) 