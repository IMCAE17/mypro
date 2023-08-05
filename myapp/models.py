from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Marks=models.IntegerField()
    Address=models.TextField()
    class Meta:
        db_table='studentlist'

class Teacher(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    Name=models.CharField(max_length=200)
    Email = models.EmailField()
    Address=models.TextField()

