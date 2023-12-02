from rest_framework.serializers import Serializer, IntegerField, ImageField


class RegisterEmployeeValidator(Serializer):
    employee = IntegerField()
    image = ImageField()


class VerifyEmployeeValidator(Serializer):
    employee = IntegerField()
    image = ImageField()
