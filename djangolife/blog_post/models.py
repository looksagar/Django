from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.title

class student(models.Model):
    name = models.CharField(max_length=120)
    roll_no = models.TextField()
    classs = models.TextField()

    def __str__(self):
        return self.name