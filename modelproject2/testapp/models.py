from django.db import models

# Create your models here.
class hydjobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=30)
    title=models.CharField(max_length=20)
    eligibility=models.CharField(max_length=30)
    address=models.TextField()
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10)

    def __str__(self) -> str:
        return f"{self.id},{self.company}"

class punejobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=30)
    title=models.CharField(max_length=20)
    eligibility=models.CharField(max_length=30)
    address=models.TextField()
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10)  

class bangjobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=30)
    title=models.CharField(max_length=20)
    eligibility=models.CharField(max_length=30)
    address=models.TextField()
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10)