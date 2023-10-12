from django.urls import include,re_path

app_name="agendamiento"

urlpatterns = [

    re_path(r'^employees/', include('agendamiento.urls.employee_urls')),  # NOQA
    re_path(r'^schedules/', include('agendamiento.urls.schedule_urls')),
    re_path(r'^statuss/', include('agendamiento.urls.status_urls')),
    re_path(r'^users/', include('agendamiento.urls.user_urls')),
    re_path(r'^validations/', include('agendamiento.urls.validation_urls')),
]
