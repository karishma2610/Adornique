from django.db import models
from .product import Product
from .customer import Customer
import datetime


class Order(models.Model):
    product=models.ForeignKey(Product,
                              on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,
                               on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    address = models.CharField(max_length=200, default='')
    phone = models.CharField(max_length=10, default='')
    date = models.DateField(default=datetime.datetime.today)
    status = models.CharField(default='Order Placed', max_length=50)
    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order\
            .objects\
            .filter(customer=customer_id)\
            .order_by('-date')
    # to get order in desc order