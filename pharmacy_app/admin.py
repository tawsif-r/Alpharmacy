from django.contrib import admin
from .models import *

model_arr = [Pharmacy_owner,Pharmacy,Medicine,Customer,Order]
for i in model_arr:
    admin.site.register(i) 