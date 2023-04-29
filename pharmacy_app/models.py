from django.db import models

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
    
    def __str__(self):
        return self.medicine_name

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
    def __str__(self):
        return str(self.customer)
    


    


    


