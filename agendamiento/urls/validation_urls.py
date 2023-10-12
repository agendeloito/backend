from django.urls import re_path
from ..views import (ValidationListView, ValidationCreateView, ValidationDetailView,
                     ValidationUpdateView, ValidationDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    re_path(r'^create/$',  # NOQA
        login_required(ValidationCreateView.as_view()),
        name="validation_create"),

    re_path(r'^(?P<pk>\d+)/update/$',
        login_required(ValidationUpdateView.as_view()),
        name="validation_update"),

    re_path(r'^(?P<pk>\d+)/delete/$',
        login_required(ValidationDeleteView.as_view()),
        name="validation_delete"),

    re_path(r'^(?P<pk>\d+)/$',
        ValidationDetailView.as_view(),
        name="validation_detail"),

    re_path(r'^$',
        ValidationListView.as_view(),
        name="validation_list"),
]
