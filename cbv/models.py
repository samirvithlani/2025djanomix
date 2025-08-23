from django.db import models

# Create your models here.


class Sports(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    no_player = models.PositiveIntegerField()
    
    class Meta:
        db_table="sports"
    
    def __str__(self):
        return self.name    