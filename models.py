from django.db import models

# This is a model representing a car
class Car(models.Model):
    car_id = models.AutoField(primary_key=True) 
    serial_number = models.CharField(max_length=50, unique=True)  
    make = models.CharField(max_length=50)  
    model = models.CharField(max_length=50)  
    colour = models.CharField(max_length=30)  
    year = models.IntegerField()  
    car_for_sale = models.BooleanField()  

# This is a model representing a customer
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)  
    last_name = models.CharField(max_length=50)  
    first_name = models.CharField(max_length=50)  
    phone_number = models.CharField(max_length=15)  
    address = models.TextField()  
    city = models.CharField(max_length=50)  
    state_province = models.CharField(max_length=50)  
    country = models.CharField(max_length=50)  
    postal_code = models.CharField(max_length=20)  

# This is a model representing a salesperson
class Salesperson(models.Model):
    salesperson_id = models.AutoField(primary_key=True)  
    last_name = models.CharField(max_length=50)  
    first_name = models.CharField(max_length=50)  

# This is a model representing a sales invoice
class Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)  
    invoice_number = models.CharField(max_length=50, unique=True)  
    date = models.DateField()  # Invoice date
    car = models.ForeignKey(Car, on_delete=models.CASCADE) 
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) 
    salesperson = models.ForeignKey(Salesperson, on_delete=models.CASCADE)  

# this is a model representing a service ticket
class ServiceTicket(models.Model):
    service_ticket_id = models.AutoField(primary_key=True)  
    service_ticket_number = models.CharField(max_length=50, unique=True) 
    car = models.ForeignKey(Car, on_delete=models.CASCADE)  
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  
    date_received = models.DateField()  
    comments = models.TextField()  
    date_returned = models.DateField(null=True, blank=True)  

# This is a model representing a service type
class Service(models.Model):
    service_id = models.AutoField(primary_key=True)  
    service_name = models.CharField(max_length=100)  
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)  

# This is a model representing a mechanic
class Mechanic(models.Model):
    mechanic_id = models.AutoField(primary_key=True)  
    last_name = models.CharField(max_length=50)  
    first_name = models.CharField(max_length=50) 

# This is  model representing the relationship between mechanics, services, and service tickets
class ServiceMechanic(models.Model):
    service_mechanic_id = models.AutoField(primary_key=True)  
    service_ticket = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)  
    service = models.ForeignKey(Service, on_delete=models.CASCADE)  
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)  
    hours = models.DecimalField(max_digits=5, decimal_places=2)  
    comment = models.TextField()  
    rate = models.DecimalField(max_digits=10, decimal_places=2) 

# This is a model representing car parts
class Part(models.Model):
    part_id = models.AutoField(primary_key=True)  
    part_number = models.CharField(max_length=50, unique=True)  
    description = models.TextField() 
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)  
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)  

# This is a model representing parts used in a service
class PartsUsed(models.Model):
    parts_used_id = models.AutoField(primary_key=True)  
    part = models.ForeignKey(Part, on_delete=models.CASCADE)  
    service_ticket = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)  
    number_used = models.IntegerField()  
    price = models.DecimalField(max_digits=10, decimal_places=2)  