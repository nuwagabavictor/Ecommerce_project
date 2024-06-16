from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='products/')
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    First_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=20)
    Email = models.EmailField(unique=True)
    Phone_number = models.CharField(max_length=15, blank=True, null=True)
    Address = models.TextField(blank='True', null='True')

    def __str__(self):
        return f"{self.First_name}{self.Last_name}{self.Email}"

