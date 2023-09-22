from django.db import models

class Drink(models.Model):
    name = models.CharField('Name', max_length=250)
    description = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name