# students/models.py
from djongo import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField(unique=True)
    age = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self):
        return self.name
