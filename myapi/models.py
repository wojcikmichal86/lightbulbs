from django.db import models

class Lightbulb(models.Model):
    name=models.CharField(max_length=20)
    turned_on = models.BooleanField()

    def __str__(self):
        return self.name

# Create your models here.
