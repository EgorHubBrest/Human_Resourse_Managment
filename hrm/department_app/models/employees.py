"""Django models"""
from django.db import models
from djmoney.models.fields import MoneyField 


class Employees(models.Model):
    """Employees"""
    Id = models.IntegerField('ID')
    name = models.CharField('Name',max_length=50)
    department = models.CharField('Department',max_length=50)
    salary = MoneyField('Salary',max_digits=14, decimal_places=2, default_currency='USD')
    date = models.DateField('Date of birthday')
    email = models.EmailField('Email')
    status = models.CharField('Active',max_length=50)


    def __str__(self):
        return str(self.name)
