from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    phone = models.IntegerField()
    address = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class StudentImage(models.Model):
    image = models.ImageField(upload_to='know/')
    student  = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="students") 
    
