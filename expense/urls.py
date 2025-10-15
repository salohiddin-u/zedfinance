from django.urls import path

from .views import *

urlpatterns = [
    path("", DashboardTemplateView.as_view(), name="dashboard"),
    path("budgets/", BudgetsTemplateView.as_view(), name="budgets"),
]