from django.urls import path
from .views import (
    EmployeeAPIView,
    EmployeeDetailAPIView,
    RegisterEmployeeAPIView,
    VerifyEmployeeAPIView,
)

urlpatterns = [
    path("", EmployeeAPIView.as_view()),
    path("<int:employeeId>/", EmployeeDetailAPIView.as_view()),
    path("register/", RegisterEmployeeAPIView.as_view()),
    path("verify/", VerifyEmployeeAPIView.as_view()),
]
