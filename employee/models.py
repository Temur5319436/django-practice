from django.db import models
from branch.models import Branch

# Create your models here.

GENDER = [
    ("MALE", "MALE"),
    ("FEMALE", "FEMALE"),
]


class Employee(models.Model):
    full_name = models.CharField(max_length=255, unique=True)

    birth_day = models.DateField()

    gender = models.CharField(choices=GENDER, max_length=6)

    branch = models.ForeignKey(
        Branch, on_delete=models.CASCADE, related_name="employees", null=True
    )

    image = models.JSONField()

    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        db_table = "employees"

    def __str__(self) -> str:
        return self.full_name
