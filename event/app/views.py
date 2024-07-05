from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Event, Participant
from .forms import EventForm, ParticipantForm


@login_required(login_url='login')
def events(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            return redirect('events')
    else:
        form = EventForm()
    events = Event.objects.all()
    ctx = {
        'events': events,
        'form': form
    }
    return render(request, 'app/events.html', ctx)


@login_required(login_url='login')
def event_info(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
    else:
        form = EventForm(instance=event)
    ctx = {
        'event': event,
        'form': form
    }
    return render(request, 'app/event_info.html', ctx)


@login_required(login_url='login')
def event_delete(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('events')
    return redirect('event_info', event_id=event_id)


@login_required(login_url='login')
def participants(request):
    participants = Participant.objects.all()
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            participant = form.save(commit=False)
            participant.user = request.user
            participant.save()
            form.save_m2m()

    else:
        form = ParticipantForm()
    ctx = {
        'participants': participants,
        'form': form
    }
    return render(request, 'app/participants.html', ctx)


@login_required(login_url='login')
def participant_info(request, participant_id):
    participant = Participant.objects.get(id=participant_id)
    if request.method == 'POST':
        form = ParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            participant = form.save(commit=False)
            participant.user = request.user
            participant.save()
            form.save_m2m()


    else:
        form = ParticipantForm(instance=participant)
    ctx = {
        'participant': participant,
        'form': form
    }
    return render(request, 'app/participant_info.html', ctx)


def participant_delete(request, participant_id):
    participant = Participant.objects.get(id=participant_id)
    if request.method == 'POST':
        participant.delete()
        return redirect('participants')
    return redirect('participant_info', participant_id=participant_id)
