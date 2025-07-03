from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import CheckIn



from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! Please login.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


@login_required
def dashboard(request):
    today = timezone.localdate()
    checkin = CheckIn.objects.filter(user=request.user, date=today).first()
    return render(request, 'accounts/dashboard.html', {'user': request.user, 'checkin': checkin})


@login_required
def check_in(request):
    if request.method == 'POST':
        today = timezone.localdate()
        current_local_time = timezone.localtime()

        checkin, created = CheckIn.objects.get_or_create(user=request.user, date=today)
        checkin.checked_in = True
        checkin.checkin_time = current_local_time.time()
        checkin.save()

        return redirect('dashboard')
    return redirect('dashboard')





