from django.contrib import admin
from shop.models import product, Order
#from shop.models import Orders
# Register your models here.
admin.site.register(product)
admin.site.register(Order)
