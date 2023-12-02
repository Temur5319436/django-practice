from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Branch
from .serializers import BranchSerializer


class BranchAPIView(ListCreateAPIView):
    queryset = Branch.objects.all()

    serializer_class = BranchSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        if "search" in self.request.GET:
            queryset = queryset.filter(name__contains=self.request.GET.get("search"))

        return queryset


class BranchDetailAPIView(RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = "branchId"

    queryset = Branch.objects.all()

    serializer_class = BranchSerializer
