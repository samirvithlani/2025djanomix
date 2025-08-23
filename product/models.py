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
        

modelchoice = (("suv","SUV"),("hatchback","hatchback"),("sedan","SEDAN"))

class Model(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    modeltype = models.CharField(choices=modelchoice)
    
    class Meta:
        db_table = "models"

    def __str__(self):
        return self.name
class Car(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(choices=(("red","red"),("white","white"),("black","black")))        
    price = models.PositiveIntegerField()
    model = models.ForeignKey(Model,on_delete=models.CASCADE,related_name="model")
    
    class Meta:
        db_table="car"