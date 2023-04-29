from django.forms import ModelForm
from .models import *


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__' # if not all than list them like ['customer','medicine','total_bill']


class MedicineForm(ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__' 