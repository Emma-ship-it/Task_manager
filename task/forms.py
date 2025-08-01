from django import forms
from .models import Tasks
class CreateTaskForm(forms.ModelForm):
    class Meta:
        model =Tasks
        fields= ['title','description','due_date','category','priority']