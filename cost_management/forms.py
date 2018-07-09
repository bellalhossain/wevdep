from django import forms
from .models import Expense
#from .models import Expenseaaa

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
		
#class ExpenseaaaForm(forms.ModelForm):
    #class Meta:
        #model = Expenseaaa
        #fields = '__all__'