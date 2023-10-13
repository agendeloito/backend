#from django.conf.urls import url
from django.urls import path, include
from .views import (
    EmployeesListApiView,
)

urlpatterns = [
    path('api', EmployeesListApiView.as_view()),
]