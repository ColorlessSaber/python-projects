from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction

# render the home page when requested
def home(request):
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        pk = request.POST['account'] # retrieve which account the user wants to view
        return balance(request, pk)
    content = {'form': form}
    return render(request, 'checkbook/index.html', content)

# render the "Create New Account" page when requested
def create_account(request):
    form = AccountForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    content = {'form': form}
    return render(request, 'checkbook/CreateNewAccount.html', content)

# render the Balance page when requested
def balance(request, pk):
    account = get_object_or_404(Account, pk=pk) # retrieve requested account information
    transactions = Transaction.transactions.filter(account=pk) # retrieve all transactions associated with the account
    current_total = account.initial_deposit
    table_contents = {} # will hold all transaction information
    for t in transactions:
        # add or subtract from current_total based on type
        if t.type == 'Deposit':
            current_total += t.amount
        else: # withdrawal
            current_total -= t.amount
        table_contents.update({t: current_total})
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)

# render the Transaction page when requested
def transaction(request):
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            pk = request.POST['account'] # retrieve which account the user wants to view
            form.save()
            return balance(request, pk)
    content = {'form': form}
    return render(request, 'checkbook/AddTransaction.html', content)
