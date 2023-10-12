from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Validation
from ..forms import ValidationForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class ValidationListView(ListView):
    model = Validation
    template_name = "agendamiento/validation_list.html"
    paginate_by = 20
    context_object_name = "validation_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(ValidationListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ValidationListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ValidationListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(ValidationListView, self).get_queryset()

    def get_allow_empty(self):
        return super(ValidationListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(ValidationListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(ValidationListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(ValidationListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(ValidationListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(ValidationListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(ValidationListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ValidationListView, self).get_template_names()


class ValidationDetailView(DetailView):
    model = Validation
    template_name = "agendamiento/validation_detail.html"
    context_object_name = "validation"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(ValidationDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ValidationDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ValidationDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ValidationDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(ValidationDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(ValidationDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(ValidationDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ValidationDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ValidationDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ValidationDetailView, self).get_template_names()


class ValidationCreateView(CreateView):
    model = Validation
    form_class = ValidationForm
    # fields = ['rut', 'doc1', 'doc2', 'doc3', 'doc4']
    template_name = "agendamiento/validation_create.html"
    success_url = reverse_lazy("validation_list")

    def __init__(self, **kwargs):
        return super(ValidationCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(ValidationCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ValidationCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(ValidationCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(ValidationCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(ValidationCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(ValidationCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(ValidationCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(ValidationCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(ValidationCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(ValidationCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(ValidationCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ValidationCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("agendamiento:validation_detail", args=(self.object.pk,))


class ValidationUpdateView(UpdateView):
    model = Validation
    form_class = ValidationForm
    # fields = ['rut', 'doc1', 'doc2', 'doc3', 'doc4']
    template_name = "agendamiento/validation_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "validation"

    def __init__(self, **kwargs):
        return super(ValidationUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ValidationUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ValidationUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(ValidationUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ValidationUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(ValidationUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(ValidationUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(ValidationUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(ValidationUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(ValidationUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(ValidationUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(ValidationUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(ValidationUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(ValidationUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ValidationUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ValidationUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ValidationUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("agendamiento:validation_detail", args=(self.object.pk,))


class ValidationDeleteView(DeleteView):
    model = Validation
    template_name = "agendamiento/validation_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "validation"

    def __init__(self, **kwargs):
        return super(ValidationDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ValidationDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(ValidationDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(ValidationDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ValidationDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(ValidationDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(ValidationDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(ValidationDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ValidationDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ValidationDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ValidationDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("agendamiento:validation_list")
