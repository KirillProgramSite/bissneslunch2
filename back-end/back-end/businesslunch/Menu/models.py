from django.db import models
from user.models import User

class review(models.Model):
    Review = models.IntegerField(null=True, blank=True)
    speed = models.IntegerField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
         return self.comment



class Menu(models.Model):
    name = models.CharField(max_length=300)
    weight = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    compound = models.TextField(null=True, blank=True)
    calories = models.IntegerField()
    proteins = models.IntegerField()
    carbohydrates = models.IntegerField()
    fats = models.IntegerField()
    type = models.IntegerField()
    Review = models.ManyToManyField(review)

    class Meta:

        ordering = ['type']

    def __str__(self):
        return self.name



class Basket(models.Model):
    eat = models.ManyToManyField(Menu)
    name = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

