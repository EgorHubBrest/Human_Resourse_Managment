"""Django models"""
from django.db import models

class Department(models.Model):
    """Department"""

    name = models.CharField('Department',max_length=50,primary_key=True)

    Active= "Active"

    Inactive = "Inactive"

    STATUS_CHOICES = (
        (Inactive, "Inactive"),
        (Active, "Active"),
    )

    status = models.CharField(max_length=10,
                  choices=STATUS_CHOICES,
                  default="Inactive")

    def __str__(self):
        return f'Department with name {self.name}'


    class Meta:
        verbose_name = "Департамент"
        verbose_name_plural = "Департаменты"