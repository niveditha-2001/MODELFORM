from django import forms
from app.models import emp

class empform(forms.ModelForm):
    class Meta:
        model=emp
        # fields=['name','age','mob']
        fields='__all__'
        