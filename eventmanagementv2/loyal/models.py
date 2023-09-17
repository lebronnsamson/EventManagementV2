from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=69, null=False, primary_key=True)
    password = models.CharField(max_length=69, null=False)
    firstName = models.CharField(max_length=100, null=False)
    middleName = models.CharField(max_length=100, null=True)
    lastName = models.CharField(max_length=100, null=False)
    typeOfUser = models.CharField(max_length=1, choices=(('S', 'Student'), ('T', 'Teacher')))


class Student(User):
    course = models.CharField(max_length=69, null=False)
    year = models.IntegerField(default=1, null=False)
    department = models.CharField(max_length=100, null=False)

class Teacher(User):
    age = models.IntegerField(default=1, null=False, blank=False)

class TeacherSpecialization(Teacher):
    specialization = models.CharField(max_length=69, null=False)

