from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Status
from ..forms import StatusForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class StatusListView(ListView):
    model = Status
    template_name = "agendamiento/status_list.html"
    paginate_by = 20
    context_object_name = "status_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(StatusListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(StatusListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(StatusListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(StatusListView, self).get_queryset()

    def get_allow_empty(self):
        return super(StatusListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(StatusListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(StatusListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(StatusListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(StatusListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(StatusListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(StatusListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(StatusListView, self).get_template_names()


class StatusDetailView(DetailView):
    model = Status
    template_name = "agendamiento/status_detail.html"
    context_object_name = "status"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(StatusDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(StatusDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(StatusDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(StatusDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(StatusDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(StatusDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(StatusDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(StatusDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(StatusDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(StatusDetailView, self).get_template_names()


class StatusCreateView(CreateView):
    model = Status
    form_class = StatusForm
    # fields = ['id_status', 'description']
    template_name = "agendamiento/status_create.html"
    success_url = reverse_lazy("status_list")

    def __init__(self, **kwargs):
        return super(StatusCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(StatusCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(StatusCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(StatusCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(StatusCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(StatusCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(StatusCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(StatusCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(StatusCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(StatusCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(StatusCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(StatusCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(StatusCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("agendamiento:status_detail", args=(self.object.pk,))


class StatusUpdateView(UpdateView):
    model = Status
    form_class = StatusForm
    # fields = ['id_status', 'description']
    template_name = "agendamiento/status_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "status"

    def __init__(self, **kwargs):
        return super(StatusUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(StatusUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(StatusUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(StatusUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(StatusUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(StatusUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(StatusUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(StatusUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(StatusUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(StatusUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(StatusUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(StatusUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(StatusUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(StatusUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(StatusUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(StatusUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(StatusUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("agendamiento:status_detail", args=(self.object.pk,))


class StatusDeleteView(DeleteView):
    model = Status
    template_name = "agendamiento/status_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "status"

    def __init__(self, **kwargs):
        return super(StatusDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(StatusDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(StatusDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(StatusDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(StatusDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(StatusDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(StatusDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(StatusDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(StatusDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(StatusDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(StatusDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("agendamiento:status_list")
