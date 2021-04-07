"""Django models"""
from django.db import models


class Department(models.Model):
    """Department"""

    id = models.BigAutoField(primary_key=True)

    name = models.CharField('Department', max_length=50,
                            null=False, default='Name department')

    Active = "Active"

    Inactive = "Inactive"

    STATUS_CHOICES = (
        (Inactive, "Inactive"),
        (Active, "Active"),
    )

    status_departmnet = models.CharField(max_length=8,
                              choices=STATUS_CHOICES,
                              default="Inactive")

    def __str__(self):
        return f'Department with name {self.name}'

    class Meta:
        """Departmnet"""
        verbose_name = "Departmnet"
        verbose_name_plural = "Departmnets"
