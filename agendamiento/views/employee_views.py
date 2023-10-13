from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Employee
from ..forms import EmployeeForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse

class EmployeeListView(ListView):
    model = Employee
    template_name = "agendamiento/employee_list.html"
    paginate_by = 20
    context_object_name = "employee_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    

    def __init__(self, **kwargs):
        return super(EmployeeListView, self).__init__(**kwargs)


    def get(self, request, *args, **kwargs):

        employees = Employee.objects.all()

        data = serializers.serialize('json', employees)
        #return HttpResponse(employees, content_type='application/json')
        return JsonResponse(employees,safe=False)



class EmployeeDetailView(DetailView):
    model = Employee
    template_name = "agendamiento/employee_detail.html"
    context_object_name = "employee"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(EmployeeDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(EmployeeDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(EmployeeDetailView, self).get(request, *args, **kwargs)



class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    # fields = ['rut', 'name', 'lastname', 'status']
    template_name = "agendamiento/employee_create.html"
    success_url = reverse_lazy("employee_list")

    def __init__(self, **kwargs):
        return super(EmployeeCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(EmployeeCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(EmployeeCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(EmployeeCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(EmployeeCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(EmployeeCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(EmployeeCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(EmployeeCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(EmployeeCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(EmployeeCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(EmployeeCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(EmployeeCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(EmployeeCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("agendamiento:employee_detail", args=(self.object.pk,))


class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    # fields = ['rut', 'name', 'lastname', 'id_status']
    template_name = "agendamiento/employee_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "employee"

    def __init__(self, **kwargs):
        return super(EmployeeUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(EmployeeUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(EmployeeUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(EmployeeUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(EmployeeUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(EmployeeUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(EmployeeUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(EmployeeUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(EmployeeUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(EmployeeUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(EmployeeUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(EmployeeUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(EmployeeUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(EmployeeUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(EmployeeUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(EmployeeUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(EmployeeUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("agendamiento:employee_detail", args=(self.object.pk,))


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = "agendamiento/employee_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "employee"

    def __init__(self, **kwargs):
        return super(EmployeeDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(EmployeeDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(EmployeeDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(EmployeeDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(EmployeeDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(EmployeeDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(EmployeeDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(EmployeeDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(EmployeeDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(EmployeeDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(EmployeeDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("agendamiento:employee_list")
