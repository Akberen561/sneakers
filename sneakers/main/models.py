from django.db import models

# Create your models here.
class Client(models.Models):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    id = models.IntegerField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.id

class sneakers(models.Model):
    brand = models.CharField(max_length=30)
    name = models.CharField(max_length = 30)
    price = models.IntegerField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.ordering

class admin(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    id = models.IntegerField()