# Register your models here.
from django.contrib import admin
from .models import *

model_arr = [Finaled_order]
for i in model_arr:
    admin.site.register(i) 