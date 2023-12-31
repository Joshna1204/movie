from django import forms
from mov.models import Cards
class editform(forms.ModelForm):
    class Meta:
        model=Cards
        fields='__all__'