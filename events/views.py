from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EventUploadForm


@login_required
def upload_event(request):

    if request.method == 'POST':

        form = EventUploadForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            event = form.save(commit=False)

            event.student = request.user

            event.save()

            return redirect('student_dashboard')

    else:
        form = EventUploadForm()

    return render(
        request,
        'events/upload_event.html',
        {'form': form}
    )