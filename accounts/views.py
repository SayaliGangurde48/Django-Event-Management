from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import StudentRegistrationForm
from events.models import EventUpload


def home(request):
    return render(request, 'accounts/home.html')


def register(request):

    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = StudentRegistrationForm()

    return render(
        request,
        'accounts/register.html',
        {'form': form}
    )


def user_login(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect('student_dashboard')

    else:
        form = AuthenticationForm()

    return render(
        request,
        'accounts/login.html',
        {'form': form}
    )


@login_required
def student_dashboard(request):

    uploaded_events = EventUpload.objects.filter(
        student=request.user
    ).order_by('-uploaded_at')

    context = {
        'user': request.user,
        'total_events': uploaded_events.count(),
        'uploaded_events': uploaded_events,
    }

    return render(
        request,
        'accounts/student_dashboard.html',
        context
    )


@login_required
def user_logout(request):

    logout(request)

    return redirect('login')