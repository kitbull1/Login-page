from django.db import models

# Create your models here.
class destination(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(1)
    

    