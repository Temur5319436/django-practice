from datetime import date, datetime
from rest_framework.serializers import ModelSerializer, ValidationError, DateField

from .models import Employee
from branch.models import Branch


class EmployeeSerializer(ModelSerializer):
    birth_day = DateField(format="%d.%m.%Y")

    class Meta:
        model = Employee
        fields = ["id", "full_name", "birth_day", "gender"]

    def validate_full_name(self, value: str):
        if not value.upper() == value:
            raise ValidationError("Full name of employee should be uppercase!")

        return value

    def validate_birth_day(self, birth_day: date):
        now = datetime.now()

        if birth_day.year > now.year - 18:
            raise ValidationError("Age of employee should be higher that 18+!")

        return birth_day

    def create(self, validated_data):
        validated_data["image"] = {"image": [], "path": None}

        return Employee.objects.create(**validated_data)


class BranchItemSerializer(ModelSerializer):
    class Meta:
        model = Branch
        fields = ["id", "name"]


class VerifiedEmployeeSerializer(ModelSerializer):
    branch = BranchItemSerializer()

    class Meta:
        model = Employee
        fields = ["id", "full_name", "birth_day", "branch", "gender", "created_at"]
