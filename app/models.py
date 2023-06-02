from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
# Create your models here.

State={
    ('Bihar','Bihar'),
    ('Maharastra','Maharastra')
}
class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=80)
    locality=models.CharField(max_length=80)
    city=models.CharField(max_length=80)
    zipcode=models.IntegerField()
    state=models.CharField(choices=State,max_length=80)

    def __str__(self):
        return str(self.id)
Category_choices={
    ('M','Mobile'),
    ('L','Laptop'),
    ('TW','TopWear'),
    ('BW','BottomWear')
}      
class Product(models.Model):
    title=models.CharField(max_length=80)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    brand=models.CharField(max_length=80)
    category=models.CharField(choices=Category_choices,max_length=80)
    product_img=models.ImageField(upload_to='productimg') 

def __str__(self):
        return str(self.id)       

class Cart(models.Model):
            user=models.ForeignKey(User,on_delete=models.CASCADE)
            product=models.ForeignKey(Product,on_delete=models.CASCADE)
            quantity=models.PositiveIntegerField(default=1)

def __str__(self):
        return str(self.id)   

class Orderplaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=80)

    def __str__(self):
        return str(self.id)


