from rest_framework.serializers import Serializer, IntegerField, ImageField


class RegisterEmployeeValidator(Serializer):
    employee_id = IntegerField()
    branch_id = IntegerField()
    image = ImageField()


class VerifyEmployeeValidator(Serializer):
    employee = IntegerField()
    image = ImageField()
