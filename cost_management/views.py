from django.shortcuts import render, redirect
from .models import Expense
#from .models import Expenseaaa
from .forms import ExpenseForm
#from .forms import ExpenseaaaForm


def my_expense(request):
    expenses = Expense.objects.all()
    context = {'expenses': expenses}
    return render(request, 'cost/expense.html', context)

#def my_expenseaaa(request):
    #expenses = Expenseaaa.objects.all()
    #context = {'expenses': expenses}
    #return render(request, 'cost/expenseaaa.html', context)


def add_expense(request):

    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        form.save()
        return redirect('cost-list')

    else:
        form = ExpenseForm
    return render(request, 'cost/add_expense.html', {'form': form})


def edit_expense(request, expense_id):
    expense = Expense.objects.get(id=expense_id)
    if request.method == 'POST':
        form  = ExpenseForm(request.POST, instance=expense)
        form.save()
        return redirect('cost-list')
    else:
        form = ExpenseForm(instance=expense)
    context = {'form':form}
    return render(request, 'cost/edit_expense.html', context)


def delete_expense(request, expense_id):
    expense = Expense.objects.get(id=expense_id)
    expense.delete()
    return redirect('cost-list')
