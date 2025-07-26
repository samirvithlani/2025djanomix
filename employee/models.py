from django.db import models

# Create your models here.;
class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    age = models.PositiveIntegerField()
    salary = models.FloatField()
    status = models.BooleanField()
    joiningDate = models.DateField(null=True)
    
    
    class Meta:
        db_table = "employee"