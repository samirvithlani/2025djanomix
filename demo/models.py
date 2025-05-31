from django.db import models

# Create your models here.
#create table product (id serial pk, name varcahr(.....))
class Product(models.Model):
    rating_choice =[
        (1, '1 Star'), #radio
        (2, '2 Stars'), #radio
        (3, '3 Stars'), #radio
        (4, '4 Stars'), #radio
        (5, '5 Stars')  #radio
    ]
    name = models.CharField(max_length=100) #tex
    description = models.TextField() #textArea
    price = models.DecimalField(max_digits=10, decimal_places=2) #number
    #stock = models.IntegerField() #number
    stock = models.PositiveIntegerField() #number
    created_at = models.DateTimeField(auto_now_add=True) #dateTime
    updated_at = models.DateTimeField(auto_now=True) #dateTime
    color = models.CharField(max_length=50,null=True,blank=True) #text
    status  = models.BooleanField(default=True,null=True) #checkbox
    ratings = models.IntegerField(choices=rating_choice,default=1,null=True) #radio
    
    
    class Meta:
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-stock']
    
    def __str__(self):
        return self.name    