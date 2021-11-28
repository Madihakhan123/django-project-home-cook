from django.db import models

# Create your models here.
class product(models.Model):
    #product_id = models.AutoField(default=0)
    product_name= models.CharField(max_length=122, default="")
    category = models.CharField(max_length=50, default="")
    desc=models.TextField(default="")
    price= models.DecimalField(max_digits=10, decimal_places=2,default=0)
    pub_date = models.DateField(default=True)

#@property
#def product_id(self):
       #return self.id
def __str__(self):
        return (self.product_name)


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    #itemsjson = models.CharField(max_length=5000)
    name = models.CharField(max_length=111)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip = models.CharField(max_length=111)
    phone = models.CharField(max_length=11, default="")

def __str__(self):
    return str(self.name)
    


