from django.shortcuts import render,redirect
from .models import *
from django.forms import inlineformset_factory
from django.http import HttpResponse
from .forms import *
from .filters import OrderFilter
# Create your views here.

def home(request):
    return HttpResponse('Home')

def dashboard(request):
    # companies = Company.objects.all()
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    return render(request,'pharmacy/dashboard.html',{'orders':orders,'customers':customers,'total_customers':total_customers,'total_orders':total_orders,'delivered':delivered,'pending':pending})

def medicines(request):
    medicines = Medicine.objects.all()
    return render(request,'pharmacy/medicines.html',{'medicines':medicines})


# primary key = pk
def customers(request,pk):
    customer = Customer.objects.get(id=pk)
    # quering customers child objects from order models field
    orders = customer.order_set.all()
    order_count = orders.count()

    myFilter = OrderFilter(request.GET,queryset=orders)
    orders = myFilter.qs

    return render(request,'pharmacy/customers.html',{'myFilter':myFilter,'customer':customer,'orders':orders,'order_count':order_count})



def createOrder(request,pk):
    OrderFormSet = inlineformset_factory(Customer,Order,fields=('medicine','status'),extra=10)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
    if request.method =="POST":
        formset = OrderFormSet(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/dashboard/')

    content = {'formset':formset}
    return render(request, 'pharmacy/order_form.html',content)


def createMedicine(request):
    form = MedicineForm()
    if request.method == "POST":
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/medicines/')
    content = {'form':form}
    return render(request,'pharmacy/medicine_form.html',content)


def updateOrder(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    content = {'form':form}
    if request.method =="POST":
        # print('printing POST: ',request.POST)
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/')
    return render(request,'pharmacy/order_form.html',content)



def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    content={'item':order}
    if request.method =="POST":
        # print('printing POST: ',request.POST)
        order.delete()
        return redirect('/dashboard/')

    return render(request,'pharmacy/delete.html',content)