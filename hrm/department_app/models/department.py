"""Django models"""
from django.db import models
from djmoney.models.fields import MoneyField


class Department(models.Model):
    """Department"""
    department = models.CharField('Department',max_length=50)
    salary = MoneyField('Salary',max_digits=14, decimal_places=2, default_currency='USD')
    total_employees = models.IntegerField('Total Employees')


    def __str__(self):
        return str(self.department)
