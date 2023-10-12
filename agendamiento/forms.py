from django import forms
from .models import Employee, Schedule, Status, User, Validation


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['rut', 'name', 'lastname', 'id_status']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(EmployeeForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(EmployeeForm, self).is_valid()

    def full_clean(self):
        return super(EmployeeForm, self).full_clean()

    def clean_rut(self):
        rut = self.cleaned_data.get("rut", None)
        return rut

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_lastname(self):
        lastname = self.cleaned_data.get("lastname", None)
        return lastname

    def clean_status(self):
        id_status = self.cleaned_data.get("id_status", None)
        return id_status

    def clean(self):
        return super(EmployeeForm, self).clean()

    def validate_unique(self):
        return super(EmployeeForm, self).validate_unique()

    def save(self, commit=True):
        return super(EmployeeForm, self).save(commit)


class ScheduleForm(forms.ModelForm):

    class Meta:
        model = Schedule
        fields = ['id_schedule', 'title', 'rut', 'startdate', 'enddate']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(ScheduleForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(ScheduleForm, self).is_valid()

    def full_clean(self):
        return super(ScheduleForm, self).full_clean()

    def clean_id_schedule(self):
        id_schedule = self.cleaned_data.get("id_schedule", None)
        return id_schedule

    def clean_title(self):
        title = self.cleaned_data.get("title", None)
        return title

    def clean_rut(self):
        rut = self.cleaned_data.get("rut", None)
        return rut

    def clean_startdate(self):
        startdate = self.cleaned_data.get("startdate", None)
        return startdate

    def clean_enddate(self):
        enddate = self.cleaned_data.get("enddate", None)
        return enddate

    def clean(self):
        return super(ScheduleForm, self).clean()

    def validate_unique(self):
        return super(ScheduleForm, self).validate_unique()

    def save(self, commit=True):
        return super(ScheduleForm, self).save(commit)


class StatusForm(forms.ModelForm):

    class Meta:
        model = Status
        fields = ['id', 'description']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(StatusForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(StatusForm, self).is_valid()

    def full_clean(self):
        return super(StatusForm, self).full_clean()

    def clean_id_status(self):
        id_status = self.cleaned_data.get("id", None)
        return id_status

    def clean_description(self):
        description = self.cleaned_data.get("description", None)
        return description

    def clean(self):
        return super(StatusForm, self).clean()

    def validate_unique(self):
        return super(StatusForm, self).validate_unique()

    def save(self, commit=True):
        return super(StatusForm, self).save(commit)


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['user', 'password', 'rol']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(UserForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(UserForm, self).is_valid()

    def full_clean(self):
        return super(UserForm, self).full_clean()

    def clean_user(self):
        user = self.cleaned_data.get("user", None)
        return user

    def clean_password(self):
        password = self.cleaned_data.get("password", None)
        return password

    def clean_rol(self):
        rol = self.cleaned_data.get("rol", None)
        return rol

    def clean(self):
        return super(UserForm, self).clean()

    def validate_unique(self):
        return super(UserForm, self).validate_unique()

    def save(self, commit=True):
        return super(UserForm, self).save(commit)


class ValidationForm(forms.ModelForm):

    class Meta:
        model = Validation
        fields = ['rut', 'doc1', 'doc2', 'doc3', 'doc4']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(ValidationForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(ValidationForm, self).is_valid()

    def full_clean(self):
        return super(ValidationForm, self).full_clean()

    def clean_rut(self):
        rut = self.cleaned_data.get("rut", None)
        return rut

    def clean_doc1(self):
        doc1 = self.cleaned_data.get("doc1", None)
        return doc1

    def clean_doc2(self):
        doc2 = self.cleaned_data.get("doc2", None)
        return doc2

    def clean_doc3(self):
        doc3 = self.cleaned_data.get("doc3", None)
        return doc3

    def clean_doc4(self):
        doc4 = self.cleaned_data.get("doc4", None)
        return doc4

    def clean(self):
        return super(ValidationForm, self).clean()

    def validate_unique(self):
        return super(ValidationForm, self).validate_unique()

    def save(self, commit=True):
        return super(ValidationForm, self).save(commit)

