from rest_framework.test import APITestCase
from department_app.serializers import DepartmentSerializer, EmployeeSerializer, RegistrationSerializer
from department_app.models.employee_model import Employee
from department_app.models.department_models import Department
from department_app.models.users_models import User
from djmoney.money import Money


class SerializerTests(APITestCase):
    def test_serializer_department(self):
        dep_1 = Department.objects.create(name='Test Office', status='Active')
        dep_2 = Department.objects.create(name='Test2 Office', status='Active')
        data = DepartmentSerializer([dep_1,dep_2],many=True).data
        expected_data =[
            {
                'id':dep_1.id,
                'name':'Test Office',
                'status':'Active'
            },
            {
                'id':dep_2.id,
                'name':'Test2 Office',
                'status':'Active' 
            }
        ]
        self.assertEqual(expected_data, data)
    
    def test_serializer_employee(self):
        dep_exe = Department.objects.get(name='Executive Office')
        empl_1 = Employee.objects.create(name='Test Name', department=dep_exe, date='1986-11-01',
        salary=Money(1400, 'USD'), email='test@gmail.com', status='Active')
        empl_2 = Employee.objects.create(name='Test Name2', department=dep_exe, date='1986-11-01',
        salary=Money(1500, 'USD'), email='test2@gmail.com', status='Active')
        data = EmployeeSerializer([empl_1,empl_2],many=True).data
        expected_data =[
            {
                "id": empl_1.id,
                "name":"Test Name",
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
        self.assertEqual(expected_data, data)
    
    def test_serializer_user(self):
        us_1 = User(email='pavel1@gmail.com', username='Pavel1_Volya')
        us_2 = User(email='pavel2@gmail.com', username='Pavel2_Volya')    
        data = RegistrationSerializer([us_1,us_2],many=True).data
        expected_data =[
            {
                "email":"pavel1@gmail.com",
                "username": "Pavel1_Volya",
            },
            {
                "email":"pavel2@gmail.com",
                "username": "Pavel2_Volya",
            }
        ]
        self.assertEqual(expected_data[0]['email'], data[0]['email'])
        self.assertEqual(expected_data[0]['username'], data[0]['username'])

        self.assertEqual(expected_data[1]['email'], data[1]['email'])
        self.assertEqual(expected_data[1]['username'], data[1]['username'])
