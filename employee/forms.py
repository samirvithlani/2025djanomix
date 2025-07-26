from django.forms import ModelForm
from . import models

class EmployeeForm(ModelForm):
    class Meta:
        model = models.Employee
        fields = "__all__"
        