from django.db import models
from django.contrib.auth.models import User
class Pharmacy_owner(models.Model):
    owner_name = models.CharField(max_length=100,null=True)
    owner_phonenumber = models.PositiveIntegerField(null=True)
    owner_password = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.owner_name
    
class Pharmacy(models.Model):
    pharmacy_name = models.CharField(max_length=100,null=True)
    pharmacy_location = models.CharField(max_length=100,null=True)
    pharmacy_owner = models.OneToOneField(Pharmacy_owner,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.pharmacy_name
    

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100,null=True)
    customer_phone = models.PositiveIntegerField(null=True)
    customer_mail = models.CharField(max_length=100,null=True)
    customer_age = models.PositiveIntegerField(null=True)
    customer_password = models.CharField(max_length=100,null=True)
    customer_location = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.customer_name
    

class Medicine(models.Model):
    medicine_name = models.CharField(max_length=100,null=True)
    expire_date = models.DateField(null=True)
    group_name = models.CharField(max_length=100,null=True)
    company_name = models.CharField(max_length=100,null=True)
    price = models.PositiveIntegerField(null=True)
    digital = models.BooleanField(default=False,null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.medicine_name
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Order(models.Model):
    STATUS = (
        ('Pending','pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered'),
    )
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    total_bill = models.PositiveIntegerField(null=True)
    quantity = models.PositiveIntegerField(null=True)
    date_created = models.DateField(auto_now_add=True,null=True)
    medicine = models.ForeignKey(Medicine,null=True,on_delete=models.SET_NULL)
    status = models.CharField(max_length=100,null=True,choices=STATUS)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)
    def __str__(self):
        return str(self.customer)
    
    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 

class OrderItem(models.Model):
	product = models.ForeignKey(Medicine, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address


    


