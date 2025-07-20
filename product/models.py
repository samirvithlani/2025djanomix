from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    
    class Meta:
        db_table = "product1"
        
    def __str__(self):
        return self.name    


class Phone(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    stock = models.IntegerField()
    description = models.TextField()

    class Meta:
        db_table = "phone"

    def __str__(self):
        return self.model


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    
    class Meta:
        db_table = "contact"    