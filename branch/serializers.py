from rest_framework.serializers import ModelSerializer
from .models import Branch


class BranchSerializer(ModelSerializer):
    class Meta:
        model = Branch
        fields = ["id", "name", "address"]
