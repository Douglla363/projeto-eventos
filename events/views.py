from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import EventForm
from django.contrib import messages
from .models import Event

# Create your views here.

def index(request):

    search = request.GET.get('search')

    if (search):
        events = Event.objects.filter(title__icontains=search)

    else: 
        events = Event.objects.all().order_by('-created_at')

    return render(request, 'home.html', {'events': events})


@login_required
def create(request):

    if (request.method == "POST"):
        form = EventForm(request.POST, request.FILES)

        if (form.is_valid()):
            event = form.save(commit=False)
            event.user = request.user
            event.save()

            messages.info(request, 'Evento criado com sucesso!')

            return redirect('/')

    else:
        form = EventForm()

    return render(request, 'events/create.html', {'form': form})



def show(request, id):

    event = get_object_or_404(Event, pk=id)

    return render(request, 'events/show.html', {'event': event})


@login_required
def dashboard(request):

    events = Event.objects.all().order_by('-created_at').filter(user=request.user)

    return render(request, 'events/dashboard.html', {'events': events})



@login_required
def delete(request, id):

    event = get_object_or_404(Event, pk=id)
    event.delete()

    messages.info(request, 'Evento excluido com sucesso!')

    return redirect('/dashboard')



@login_required
def edit(request, id):

    event = get_object_or_404(Event, pk=id)
    form = EventForm(instance=event)

    if (request.method == "POST"):
        form = EventForm(request.POST, request.FILES, instance=event)

        if (form.is_valid()):
            event.save()

            messages.info(request, 'Evento editado com sucesso!')

            return redirect('/dashboard')
        else:
            return render(request, 'events/edit.html', {'form': form, 'event': event})

    else:
        return render(request, 'events/edit.html', {'form': form, 'event': event})