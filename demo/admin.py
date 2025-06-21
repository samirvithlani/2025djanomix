from django.contrib import admin
from .models import Product,Wallet,SwiggyUser,Tournament,Teams,Course,Student

# Register your models here.
admin.site.register(Product)
admin.site.register(Wallet)
admin.site.register(SwiggyUser)
admin.site.register(Tournament)
admin.site.register(Teams)
admin.site.register(Course)
admin.site.register(Student)