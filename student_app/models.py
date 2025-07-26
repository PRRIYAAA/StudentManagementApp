from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    field_of_study = models.CharField(max_length=100)
    gpa = models.FloatField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


