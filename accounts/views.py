from django.shortcuts import render

from .forms import CreateAccountForm

def create(request):
    if request.method == 'POST':
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CreateAccountForm()

    return render(request, 'create.html', {'form': form})