from rest_framework.test import APITestCase
from department_app.models.employee_model import Employee
from department_app.models.department_models import Department
from djmoney.money import Money
import json


class ModelsTests(APITestCase):
    def test_model_department(self):
        dep_1 = Department.objects.create(name='Test Office', status='Active')
        dep_2 = Department.objects.create(name='Test2 Office', status='Active')
        expected_data = [
            {
                'id': dep_1.id,
                'name': 'Test Office',
                'status': 'Active'
            },
            {
                'id': dep_2.id,
                'name': 'Test2 Office',
                'status': 'Active'
            }
        ]
        self.assertEqual(expected_data[0]['id'], dep_1.id)
        self.assertEqual(expected_data[0]['name'], dep_1.name)
        self.assertEqual(expected_data[0]['status'], dep_1.status)

        self.assertEqual(expected_data[1]['id'], dep_2.id)
        self.assertEqual(expected_data[1]['name'], dep_2.name)
        self.assertEqual(expected_data[1]['status'], dep_2.status)

    def test_model_employee(self):
        dep_exe = Department.objects.get(name='Executive Office')
        empl_1 = Employee.objects.create(name='Test Name', department=dep_exe, date='1986-11-01',
                                         salary=Money(1400, 'USD'), email='test@gmail.com', status='Active')
        empl_2 = Employee.objects.create(name='Test Name2', department=dep_exe, date='1986-11-01',
                                         salary=Money(1500, 'USD'), email='test2@gmail.com', status='Active')
        expected_data = [
            {
                "id": empl_1.id,
                "name": "Test Name",
                "date": "1986-11-01",
                "salary_currency": "USD",
                "salary": "1400.00",
                "email": "test@gmail.com",
                "status": "Active",
                "department": 1
            },
            {
                "id": empl_2.id,
                "name": "Test Name2",
                "date": "1986-11-01",
                "salary_currency": "USD",
                "salary": "1500.00",
                "email": "test2@gmail.com",
                "status": "Active",
                "department": 1
            }
        ]
        self.assertEqual(expected_data[0]['id'], empl_1.id)
        self.assertEqual(expected_data[0]['name'], empl_1.name)
        self.assertEqual(expected_data[0]['date'], empl_1.date)
        self.assertEqual(expected_data[0]['email'], empl_1.email)

        self.assertEqual(expected_data[1]['id'], empl_2.id)
        self.assertEqual(expected_data[1]['name'], empl_2.name)
        self.assertEqual(expected_data[1]['date'], empl_2.date)
        self.assertEqual(expected_data[1]['email'], empl_2.email)
