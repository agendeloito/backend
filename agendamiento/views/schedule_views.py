from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Schedule
from ..forms import ScheduleForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class ScheduleListView(ListView):
    model = Schedule
    template_name = "agendamiento/schedule_list.html"
    paginate_by = 20
    context_object_name = "schedule_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(ScheduleListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ScheduleListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ScheduleListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(ScheduleListView, self).get_queryset()

    def get_allow_empty(self):
        return super(ScheduleListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(ScheduleListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(ScheduleListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(ScheduleListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(ScheduleListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(ScheduleListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(ScheduleListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ScheduleListView, self).get_template_names()


class ScheduleDetailView(DetailView):
    model = Schedule
    template_name = "agendamiento/schedule_detail.html"
    context_object_name = "schedule"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(ScheduleDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ScheduleDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ScheduleDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ScheduleDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(ScheduleDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(ScheduleDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(ScheduleDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ScheduleDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ScheduleDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ScheduleDetailView, self).get_template_names()


class ScheduleCreateView(CreateView):
    model = Schedule
    form_class = ScheduleForm
    # fields = ['id_schedule', 'title', 'rut', 'startdate', 'enddate']
    template_name = "agendamiento/schedule_create.html"
    success_url = reverse_lazy("schedule_list")

    def __init__(self, **kwargs):
        return super(ScheduleCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(ScheduleCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ScheduleCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(ScheduleCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(ScheduleCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(ScheduleCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(ScheduleCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(ScheduleCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(ScheduleCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(ScheduleCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(ScheduleCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(ScheduleCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ScheduleCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("agendamiento:schedule_detail", args=(self.object.pk,))


class ScheduleUpdateView(UpdateView):
    model = Schedule
    form_class = ScheduleForm
    # fields = ['id_schedule', 'title', 'rut', 'startdate', 'enddate']
    template_name = "agendamiento/schedule_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "schedule"

    def __init__(self, **kwargs):
        return super(ScheduleUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ScheduleUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ScheduleUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(ScheduleUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ScheduleUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(ScheduleUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(ScheduleUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(ScheduleUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(ScheduleUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(ScheduleUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(ScheduleUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(ScheduleUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(ScheduleUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(ScheduleUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ScheduleUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ScheduleUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ScheduleUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("agendamiento:schedule_detail", args=(self.object.pk,))


class ScheduleDeleteView(DeleteView):
    model = Schedule
    template_name = "agendamiento/schedule_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "schedule"

    def __init__(self, **kwargs):
        return super(ScheduleDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ScheduleDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(ScheduleDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(ScheduleDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ScheduleDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(ScheduleDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(ScheduleDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(ScheduleDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ScheduleDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ScheduleDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ScheduleDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("agendamiento:schedule_list")
