from django.urls import path

from employee.views import DetailEmployee, ListEmployee

urlpatterns = [
    path('', ListEmployee.as_view()),
    path('<int:pk>/', DetailEmployee.as_view()),
]