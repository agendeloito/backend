from django.urls import re_path
from ..views import (ScheduleListView, ScheduleCreateView, ScheduleDetailView,
                     ScheduleUpdateView, ScheduleDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    re_path(r'^create/$',  # NOQA
        login_required(ScheduleCreateView.as_view()),
        name="schedule_create"),

    re_path(r'^(?P<pk>\d+)/update/$',
        login_required(ScheduleUpdateView.as_view()),
        name="schedule_update"),

    re_path(r'^(?P<pk>\d+)/delete/$',
        login_required(ScheduleDeleteView.as_view()),
        name="schedule_delete"),

    re_path(r'^(?P<pk>\d+)/$',
        ScheduleDetailView.as_view(),
        name="schedule_detail"),

    re_path(r'^$',
        ScheduleListView.as_view(),
        name="schedule_list"),
]
