from django.urls import re_path
from ..views import (StatusListView, StatusCreateView, StatusDetailView,
                     StatusUpdateView, StatusDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    re_path(r'^create/$',  # NOQA
        login_required(StatusCreateView.as_view()),
        name="status_create"),

    re_path(r'^(?P<pk>\d+)/update/$',
        login_required(StatusUpdateView.as_view()),
        name="status_update"),

    re_path(r'^(?P<pk>\d+)/delete/$',
        login_required(StatusDeleteView.as_view()),
        name="status_delete"),

    re_path(r'^(?P<pk>\d+)/$',
        StatusDetailView.as_view(),
        name="status_detail"),

    re_path(r'^$',
        StatusListView.as_view(),
        name="status_list"),
]
