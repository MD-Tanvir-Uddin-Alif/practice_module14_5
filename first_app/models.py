from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return f"Name : {self.name}"