from django.shortcuts import render

from .forms import CreateAccountForm

def create(request):
    if request.method == 'POST':
        form = CreateAccountForm(request.POST)
    else:
        form = CreateAccountForm()

    return render(request, 'create.html', {'form': form})