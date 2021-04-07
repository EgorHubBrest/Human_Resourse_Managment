"""Django models"""
from django.db import models
from department_app.models import department_models
from djmoney.models.fields import MoneyField


class Employee(models.Model):
    """Employees"""

    id = models.BigAutoField(primary_key=True)

    name = models.CharField('Name', max_length=50,
                            null=False, default='Name Person')

    department = models.ForeignKey(
        department_models.Department, on_delete=models.CASCADE, null=False, default='Name department')

    date = models.DateField('Date of birthday', default='')

    salary = MoneyField('Salary', max_digits=14,
                        decimal_places=2, default_currency='USD', default='0')

    email = models.EmailField('Email', default='')

    Active = "Active"

    Inactive = "Inactive"

    STATUS_CHOICES = (
        (Inactive, "Inactive"),
        (Active, "Active"),
    )

    status = models.CharField(max_length=8,
                              choices=STATUS_CHOICES,
                              default="Inactive")

    def __str__(self):
        return f'Employee with name {self.name} belongs to the department {self.department}'

    class Meta:
        """Employees"""
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
