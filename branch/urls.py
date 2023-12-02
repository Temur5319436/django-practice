from django.urls import path
from .views import BranchAPIView, BranchDetailAPIView

urlpatterns = [
    path("", BranchAPIView.as_view()),
    path("<int:branchId>", BranchDetailAPIView.as_view()),
]
