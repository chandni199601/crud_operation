from .models import company
from django import forms
from .models import company
class NewForm(forms.ModelForm):
    class Meta:
        model=company
        fields =('company_name',
            'company_logo',
            'company_city',
                )