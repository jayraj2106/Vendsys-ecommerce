from django.shortcuts import redirect, render
from Vendsys.accounts.forms import RegisterForm


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})
# Create your views here.
