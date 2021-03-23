"""Django models"""
from django.db import models
from department_app.models import department_models
from djmoney.models.fields import MoneyField

class Employee(models.Model):
    """Employees"""
    name = models.CharField('Name',max_length=50,primary_key=True)

    department = models.ForeignKey(department_models.Department,on_delete=models.SET_NULL,null=True)

    date = models.DateField('Date of birthday')

    salary = MoneyField('Salary',max_digits=14, decimal_places=2, default_currency='USD')

    email = models.EmailField('Email')

    Active= "Active"

    Inactive = "Inactive"

    STATUS_CHOICES = (
        (Inactive, "Inactive"),
        (Inactive, "Inactive"),
    )

    status = models.CharField(max_length=10,
                  choices=STATUS_CHOICES,
                  default="Inactive")


    def __str__(self):
        return f'Employee with name {self.name} belongs to the department {self.department}'


    class Meta:
        """Сотрудники"""
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
