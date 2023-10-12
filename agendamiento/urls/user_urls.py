from django.urls import re_path
from ..views import (UserListView, UserCreateView, UserDetailView,
                     UserUpdateView, UserDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    re_path(r'^create/$',  # NOQA
        login_required(UserCreateView.as_view()),
        name="user_create"),

    re_path(r'^(?P<pk>\d+)/update/$',
        login_required(UserUpdateView.as_view()),
        name="user_update"),

    re_path(r'^(?P<pk>\d+)/delete/$',
        login_required(UserDeleteView.as_view()),
        name="user_delete"),

    re_path(r'^(?P<pk>\d+)/$',
        UserDetailView.as_view(),
        name="user_detail"),

    re_path(r'^$',
        UserListView.as_view(),
        name="user_list"),
]
