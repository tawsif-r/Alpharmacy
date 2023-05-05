from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__' # if not all than list them like ['customer','medicine','total_bill']


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