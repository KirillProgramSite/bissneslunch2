from django.db import models
class Option(models.Model):
    title = models.CharField(max_length=150)
    score = models.IntegerField()

class Vote(models.Model):
    title = models.CharField(max_length=150, default='Какое блюдо вам больше нравится?')
    option = models.ForeignKey(Option, on_delete=models.CASCADE)

class Stories_Vote_Img(models.Model):
    vote_img = models.ImageField(upload_to='media/stories/vote')
class Storis_img(models.Model):
    img = models.ImageField(upload_to='media/stories/default')

class Storis(models.Model):
    storis = models.ForeignKey(Storis_img, on_delete=models.CASCADE)

class Stories_Vote(models.Model):
    img = models.ForeignKey(Stories_Vote_Img, on_delete=models.CASCADE)
    vote = models.ManyToManyField(Vote)






# Create your models here.
