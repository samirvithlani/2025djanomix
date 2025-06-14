from django.contrib import admin
from .models import Product,Wallet,SwiggyUser

# Register your models here.
admin.site.register(Product)
admin.site.register(Wallet)
admin.site.register(SwiggyUser)