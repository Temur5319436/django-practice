from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from .models import Employee
from .serializers import EmployeeSerializer
from .validators import RegisterEmployeeValidator, VerifyEmployeeValidator
from .utils import store_image
from control.settings import BASE_DIR

import face_recognition
import os


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


class RegisterEmployeeAPIView(APIView):
    def post(self, request: Request):
        RegisterEmployeeValidator(data=request.data).is_valid(raise_exception=True)

        path = store_image(request.FILES.get("image"))

        image = face_recognition.load_image_file(f"{BASE_DIR}{path}")
        locations = face_recognition.face_locations(image)

        if not locations:
            return Response(
                {"result": "There is not face in image!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if len(locations) != 1:
            return Response(
                {"error": "Image should contain exactly one face!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        face = face_recognition.face_encodings(image)[0]

        Employee.objects.filter(id=request.POST.get("employee_id")).update(
            image={"path": path, "image": face.tolist()},
            branch_id=request.POST.get("branch_id"),
        )

        return Response(
            {
                "message": "Employee is registered!",
                "path": path,
            }
        )


class VerifyEmployeeAPIView(APIView):
    def post(self, request: Request):
        VerifyEmployeeValidator(data=request.data).is_valid(raise_exception=True)

        employee = Employee.objects.filter(id=request.POST.get("employee")).first()

        path = f"{BASE_DIR}%s" % store_image(request.FILES.get("image"))

        image = face_recognition.load_image_file(path)
        locations = face_recognition.face_locations(image)

        # Delete trash image
        os.remove(path)

        if not locations:
            return Response(
                {"result": "There is not face in image!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if len(locations) != 1:
            return Response(
                {"error": "Image should contain exactly one face!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        face = face_recognition.face_encodings(image)[0]

        # Compare the face encodings
        match = face_recognition.compare_faces([employee.image["image"]], face)[0]

        if match:
            return Response(
                {"message": "Employee is verified!"}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"message": "Employee is not verified!"},
                status=status.HTTP_400_BAD_REQUEST,
            )
