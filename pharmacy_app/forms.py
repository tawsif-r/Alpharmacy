from django.forms import ModelForm
from store.models import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__' 

class Finaled_orderForm(ModelForm):
    class Meta:
        model = Finaled_order
        fields = '__all__' 
class MedicineForm(ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__' 

class RegisterForm(ModelForm):
    class Meta:
        model = Pharmacy_owner
        fields = '__all__'
        exclude = ['owner_phonenumber']
        labels = {
            'owner_name': 'Username',
            'owner_password':'Password',
            
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']