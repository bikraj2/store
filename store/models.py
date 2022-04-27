from colorsys import ONE_SIXTH
from configparser import MAX_INTERPOLATION_DEPTH
from operator import mod
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey(
        'Product',on_delete=models.SET_NULL,null=True,related_name='+'
    )


class Product(models.Model):
    title = models.CharField(null=False,max_length=245) #varchar of 245
    descirptions = models.TextField(max_length=1000)
    #max price = 9999.99
    price = models.DecimalField(null=False,max_digits=4,decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateField(auto_now_add=True)
    collection = models.ForeignKey(
        Collection,on_delete=models.PROTECT
    )
    promotions = models.ManyToManyField(
        Promotion
    )
#model to store user information
class Customer(models.Model):
    MEMBERSHIP_BRONZE='B'
    MEMBERSHIP_SILVER='S'
    MEMBERSHIP_GOLD='G'

    MEMBERSHIP_CHOICES =[
        (MEMBERSHIP_BRONZE,'Bronze'),
        (MEMBERSHIP_SILVER,'Silver'),
        (MEMBERSHIP_GOLD,'Gold')
    ]
    first_name = models.CharField(null=False,max_length=25)# varchar  25
    last_name = models.CharField(null=False,max_length=25)
    middle_name = models.CharField(null=True,max_length=25)
    email = models.EmailField(unique=True)
    phone = models.PositiveBigIntegerField()
    birth_date= models.DateField(null=True)
    membership= models.CharField(max_length=1,choices=MEMBERSHIP_CHOICES,default=MEMBERSHIP_BRONZE)

class Order(models.Model):
    PENDING='P'
    COMPLETED = 'C'
    FAILED = 'F'
    PAYMENT_STATUS=[
        (PENDING,'PENDING'),
        (COMPLETED,'COMPLETED'),
        (FAILED,'FAILED')   
    ]
    customer = models.ForeignKey(
        Customer,on_delete=models.PROTECT
    )
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1,choices=PAYMENT_STATUS,default=PENDING)


class Address (models.Model):
    street=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    Customer=models.ForeignKey(
        Customer,on_delete=models.CASCADE)


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity = models.PositiveBigIntegerField(max_length=99,)
    unit_price = models.DecimalField(max_digits=6,decimal_places=2)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)



class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,on_delete=models.CASCADE
    )
    quantity = models.PositiveSmallIntegerField()
