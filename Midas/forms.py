from django.forms import ModelForm
from django import forms
from .models import Income, Expenses
from django.forms import formset_factory

class RecordIncomeForm(ModelForm):
    class Meta:
        model = Income
        fields = ['category', 'cost', 'date']
        
class RecordExpensesForm(ModelForm):
    # user = forms.TextInput(widget=forms.HiddenInput(), initial=123)
    class Meta:
        model = Expenses
        fields = ['user', 'category', 'cost', 'date']
        widgets = {
            'user': forms.HiddenInput()
        }

FormSet = formset_factory(RecordIncomeForm,RecordExpensesForm)