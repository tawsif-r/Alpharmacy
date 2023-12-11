from django.shortcuts import render,redirect
from store.models import *
from .models import *
from django.forms import inlineformset_factory
from django.http import HttpResponse
from .forms import *
from .filters import *
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect("dashboard")
            else:
                messages.info(request,'username or password is wrong')
        context = {}
        return render(request,"pharmacy/login.html",context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,"Account created for "+ user)
                return redirect('login')


    context = {'form':form}
    return render(request,"pharmacy/register.html",context)

@login_required(login_url='login')
def dashboard(request):
    
    orders = Order.objects.all() #not using this
    finaled_order = Finaled_order.objects.all()  # using this model right now
    myFilter = FinaledOrderFilter(request.GET,queryset=finaled_order)
    finaled_order = myFilter.qs
    # customers = Customer.objects.all() #not using this
    # total_customers = customers.count() #not using this
    total_customers = finaled_order.count()
    total_orders = finaled_order.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    return render(request,'pharmacy/dashboard.html',{'orders':orders,'customers':customers,'total_customers':total_customers,'total_orders':total_orders,'delivered':delivered,'pending':pending,'finaled_order':finaled_order,'myFilter':myFilter})

@login_required(login_url='login')
def medicines(request):
    medicines = Medicine.objects.all()
    return render(request,'pharmacy/medicines.html',{'medicines':medicines})


# primary key = pk
@login_required(login_url='login')
def customers(request,pk):
    customer = Customer.objects.get(id=pk)
    # quering customers child objects from order models field
    orders = customer.order_set.all()
    order_count = orders.count()

    myFilter = OrderFilter(request.GET,queryset=orders)
    orders = myFilter.qs

    return render(request,'pharmacy/customers.html',{'myFilter':myFilter,'customer':customer,'orders':orders,'order_count':order_count})


@login_required(login_url='login')
def createOrder(request,pk):
    OrderFormSet = inlineformset_factory(Customer,Order,fields=('medicine','status'),extra=10)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
    if request.method =="POST":
        formset = OrderFormSet(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/dashboard/')

    context = {'formset':formset}
    return render(request, 'pharmacy/createorder.html',context)

@login_required(login_url='login')
def createMedicine(request):
    form = MedicineForm()
    if request.method == "POST":
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/medicines/')
    context= {'form':form}
    return render(request,'pharmacy/medicine_form.html',context)

@login_required(login_url='login')
def updateOrder(request,pk):
    order = Finaled_order.objects.get(id=pk)
    form = Finaled_orderForm(instance=order)
    
    if request.method =="POST":
        
        form = Finaled_orderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/')
    context = {'form':form}
    return render(request,'pharmacy/order_form.html',context)


@login_required(login_url='login')
def deleteOrder(request,pk):
    order = Finaled_order.objects.get(id=pk)
    context={'item':order}
    if request.method =="POST":
        # print('printing POST: ',request.POST)
        order.delete()
        return redirect('/dashboard/')

    return render(request,'pharmacy/delete.html',context)


