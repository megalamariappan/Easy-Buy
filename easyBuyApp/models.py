from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from decimal import Decimal

# Create your models here.
class categories(models.Model):
    category=models.CharField(max_length=50,null=False,blank=False)
    
    def __str__(self):
        return self.category
    
class offer(models.Model):
    offer_percent=models.IntegerField(null=False,blank=False)
    
    def __str__(self):
        return f"{self.offer_percent}%"
        
class products(models.Model):
    product_name=models.CharField(max_length=200,null=False,blank=False)
    category_name=models.ForeignKey(categories,on_delete=models.CASCADE)
    product_image=models.ImageField(upload_to="images/",null=False,blank=False)
    original_price=models.DecimalField(max_digits=10,decimal_places=2,null=False,blank=False)
    discount=models.ForeignKey(offer,on_delete=models.CASCADE)
    discount_amount=models.DecimalField(max_digits=10,decimal_places=2,editable=False)
    pattern=models.CharField(max_length=100,null=True,blank=True)
    netquantity=models.IntegerField(null=True,blank=True)
    sizes=MultiSelectField(max_length=50,null=True,blank=True,choices=[
        ('S','S'),
        ('M','M'),
        ('L','L'),
        ('XL','XL'),
        (6,6),
        (7,7),
        (8,8),
        (9,9),
        (10,10),
    ])
    country_origin=models.CharField(max_length=100,null=False,blank=False)
    
    def save(self, *args, **kwargs):
        offer_percent_decimal = Decimal(self.discount.offer_percent) / Decimal(100)
        offer_s = self.original_price * offer_percent_decimal
        self.discount_amount = int(self.original_price - offer_s)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.product_name
    
class card(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    quantity=models.IntegerField(null=False,blank=False)
    total_price=models.DecimalField(editable=False,max_digits=10,decimal_places=2)
    
    def save(self,*args,**kwargs):
        self.total_price=self.product.discount_amount*self.quantity
        super().save(*args,**kwargs)
        
    def __str__(self):
        return f"{self.total_price}"

class payment(models.Model):
    payment_method=models.CharField(max_length=50)
    
    def __str__(self):
        return self.payment_method

class orders(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product_name=models.ForeignKey(products,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    name=models.CharField(max_length=50)
    email=models.EmailField()
    address=models.CharField(max_length=550)
    payments=models.ForeignKey(payment,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.quantity}"