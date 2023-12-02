from django.urls import path
from .views import EmployeeAPIView, EmployeeDetailAPIView

urlpatterns = [
    path("", EmployeeAPIView.as_view()),
    path("<int:employeeId>", EmployeeDetailAPIView.as_view()),
]
