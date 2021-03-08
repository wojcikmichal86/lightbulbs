from django.db import models

class Lightbulb(models.Model):
    name=models.CharField(max_length=20)
    turned_on = models.BooleanField()

    def __str__(self):
        return self.name



class Blinds(models.Model):
    name=models.CharField(max_length=20)
    closed = models.BooleanField()

    def __str__(self):
        return self.name



class Temperature(models.Model):
    name=models.CharField(max_length=20)
    temperature = models.IntegerField()

    def __str__(self):
        return self.name

# Create your models here.
