from django.db import models
from User.models import User
from Menu.models import Basket

class Table(models.Model):
    tabel_number = models.IntegerField()

    def __str__(self):
        return f'{self.tabel_number}'

class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    CHOICES = (
        ('1', '12:00'),
        ('2', '12:30'),
    )
    delivery_time = models.CharField(max_length=2, choices=CHOICES)

    order_table = models.ForeignKey(Table, on_delete=models.CASCADE, default=0)
    def __str__(self):
        return f"Order by {self.user.username} for basket {self.basket.id}"

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

class Application_Out(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    place = models.CharField(max_length=500)

class History_Order(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
