from django.db import models

# Create your models here.


class Branch(models.Model):
    name = models.CharField(max_length=255, unique=True)

    address = models.CharField(max_length=255, null=True)

    created_at = models.DateTimeField(null=True, auto_now_add=True)

    updated_at = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        db_table = "branches"

    def __str__(self):
        return self.name
