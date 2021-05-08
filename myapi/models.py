from django.db import models

# Create your models here.

class Hero(models.Model):
    name = models.CharField(max_length=40)
    alias = models.CharField(max_length=40)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
    