"""Django models"""
from django.db import models
from department_app.utils import STATUS_CHOICES, INACTIVE


class Department(models.Model):
    """Department"""

    id = models.BigAutoField(primary_key=True)

    name = models.CharField('Department', max_length=50,
                            null=False, default='Name department')

    status = models.CharField(max_length=8,
                              choices=STATUS_CHOICES,
                              default=INACTIVE)

    def __str__(self):
        return f'Department with name {self.name}'

    class Meta:
        """Departmnet"""
        verbose_name = "Departmnet"
        verbose_name_plural = "Departmnets"
