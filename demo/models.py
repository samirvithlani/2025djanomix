from django.db import models

# Create your models here.
#create table product (id serial pk, name varcahr(.....))
class Product(models.Model):
    name = models.CharField(max_length=100) #tex
    description = models.TextField() #textArea
    price = models.DecimalField(max_digits=10, decimal_places=2) #number
    #stock = models.IntegerField() #number
    stock = models.PositiveIntegerField() #number
    created_at = models.DateTimeField(auto_now_add=True) #dateTime
    updated_at = models.DateTimeField(auto_now=True) #dateTime
    color = models.CharField(max_length=50,null=True,blank=True) #text
    
    class Meta:
        db_table = 'product'
    
    def __str__(self):
        return self.name    