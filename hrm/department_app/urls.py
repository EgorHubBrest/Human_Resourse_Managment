"""URLS"""
from django.urls import path, include
from department_app.views.department_views import DepartmentViewSet
from department_app.views.employee_views import EmployeetViewSet
from department_app.views.user_views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView
from rest_framework.routers import DefaultRouter

app_name = 'department_app'

router = DefaultRouter()
router.register('department', DepartmentViewSet, basename='departments')
router.register('employee', EmployeetViewSet, basename='employees')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('user/', UserRetrieveUpdateAPIView.as_view(), name='user'),
    path('users/', RegistrationAPIView.as_view(), name='user-reg'),
    path('users/login/', LoginAPIView.as_view(), name='user-login'),
]
