"""URLS"""
from django.urls import path, include
from department_app.views.department_views import DepartmentViewSet
from department_app.views.employee_views import EmployeetViewSet
from department_app.views.user_views import LoginAPI, RegisterAPI, UserAPI, ChangePasswordView
from knox import views as knox_views
from rest_framework.routers import DefaultRouter


app_name = 'department_app'

router = DefaultRouter()
router.register('department', DepartmentViewSet, basename='departments')
router.register('employee', EmployeetViewSet, basename='employees')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/user/', UserAPI.as_view(), name='user'),
    path('api/change-password/', ChangePasswordView.as_view(),
         name='change-password'),
]
