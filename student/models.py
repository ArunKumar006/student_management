from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100, null=True)
    candidate_code = models.CharField(max_length=100,unique=True)
    programme = models.CharField(max_length=100, null=True)
    academic_year = models.CharField(max_length=100, null=True)


class Marks(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='mark')
    internal_mark = models.IntegerField()
    external_mark = models.IntegerField()
