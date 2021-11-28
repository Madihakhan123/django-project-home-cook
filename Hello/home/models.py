from django.db import models

# Create your models here.
class contact(models.Model):
    name= models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=11)
    desc=models.TextField()
    #date=models.DateField()
    
    def __str__(self):
        return str(self.name)
     
    
