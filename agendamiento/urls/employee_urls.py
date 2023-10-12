from django.urls import re_path
from ..views import (EmployeeListView, EmployeeCreateView, EmployeeDetailView,
                     EmployeeUpdateView, EmployeeDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    re_path(r'^create/$',  # NOQA
        login_required(EmployeeCreateView.as_view()),
        name="employee_create"),

    re_path(r'^(?P<pk>\d+)/update/$',
        login_required(EmployeeUpdateView.as_view()),
        name="employee_update"),

    re_path(r'^(?P<pk>\d+)/delete/$',
        login_required(EmployeeDeleteView.as_view()),
        name="employee_delete"),

    re_path(r'^(?P<pk>\d+)/$',
        EmployeeDetailView.as_view(),
        name="employee_detail"),

    re_path(r'^$',
        EmployeeListView.as_view(),
        name="employee_list"),
]
