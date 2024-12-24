from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=25,null=False)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True,blank=True)
    price = models.DecimalField(decimal_places=2,max_digits=5,null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
