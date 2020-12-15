from django.db import models

# Create your models here.

class Test(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()


class A(models.Model):
    onetoone = models.OneToOneField(Test)

class B(models.Model):
    pass