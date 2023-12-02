from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeAPIView(ListCreateAPIView):
    queryset = Employee.objects.only("id", "full_name", "birth_day", "gender").order_by(
        "-id"
    )
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        if "search" in self.request.GET:
            queryset = queryset.filter(
                full_name__contains=self.request.GET.get("search")
            )

        if "birth_day" in self.request.GET:
            queryset = queryset.filter(birth_day=self.request.GET.get("birth_day"))

        if "gender" in self.request.GET:
            queryset = queryset.filter(gender=self.request.GET.get("gender"))

        return queryset


class EmployeeDetailAPIView(RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = "employeeId"

    queryset = Employee.objects.only("id", "full_name", "birth_day", "gender")

    serializer_class = EmployeeSerializer
