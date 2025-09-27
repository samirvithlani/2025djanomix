from django.db import models

from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.
# BaseUserManager :
# BaseUser

class CustomeUserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("Email is Required *")
        email = self.normalize_email(email)
        user = self.model(email = email,**extra_fields)
        user.set_password(password) #hashed password
        user.save(using=self._db)
        return user
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self.create_user(email,password,**extra_fields)
    
    def get_by_natural_key(self, email):
        return self.get(email__iexact=email) 


#custom userModel
class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)    
    name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    
    USERNAME_FIELD="email"
    REQUIRED_FIELDS = ["name"]
    
    objects = CustomeUserManager()

    def __str__(self):
        return self.email
    
    class Meta:
        db_table ="CustomUser"
        
    
