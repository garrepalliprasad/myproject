from django import forms
from .models import Department,Faculty
class DepartmentForm(forms.ModelForm):
    class Meta:
        model=Department
        fields= '__all__'

class FacultyForm(forms.ModelForm):
    class Meta:
        model=Faculty
        fields=['name','doj','department']
        widgets={'doj':forms.DateInput(attrs={'type':'date'})}