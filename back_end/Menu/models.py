from django.db import models
from User.models import User

class Type(models.Model):
    Id_ru = models.IntegerField()
    name = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100)

    def __str__(self):
        return self.name_ru
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    overall_rating = models.IntegerField(null=True, blank=True)
    speed_grade = models.BooleanField(null=True, blank=True)
    taste_grade = models.BooleanField(null=True, blank=True)
    comment = models.TextField()

    def __str__(self):
        return f'{self.user}'
# Create your models here.

class Menu(models.Model):
    img = models.ImageField(upload_to='product', default="product/default.png")
    name = models.CharField(max_length=1000,)
    weight = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=3)
    desc = models.TextField()
    calorie = models.IntegerField()
    protein = models.IntegerField()
    carbohydrate = models.IntegerField()
    fat = models.IntegerField()
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    recall = models.ManyToManyField(Review, blank=True, null=True)

    class Meta:
        ordering = ['type']

    def __str__(self):
        return self.name


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    eat = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.eat}'

