from django.shortcuts import render, redirect
#import calender
#from calender import HTMLCalender
#from datetime import datetime
from .models import Event, Venue
from .forms import VenueForm, EventForm
from django.http import HttpResponseRedirect

from datetime import datetime #might use this one
from django.core.paginator import Paginator

def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('list-venues')

def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('list-events')

def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
            form.save()
            return redirect('list-events')
    return render(request, 'events/update_event.html', {'event':event,'form': form})

def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'events/add_event.html', {"form":form, 'submitted':submitted} )

def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
            form.save()
            return redirect('list-venues')
    return render(request, 'events/update_venue.html', {'venue':venue,'form': form})

def search_venues(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__contains=searched)
        return render(request, 'events/search_venues.html', {'searched':searched, 'venues':venues})
    else:
        return render(request, 'events/search_venues.html', {})

def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'events/show_venue.html', {'venue':venue})

def list_venues(request):
    venue_list = Venue.objects.all().order_by('name')

    #Set up Pagination

    p = Paginator(Venue.objects.all(), 2)
    page = request.GET.get('page')
    venues = p.get_page(page)
    nums = "a" * venues.paginator.num_pages
    return render(request, 'events/venue.html', {'venue_list':venue_list, 'venues':venues, 'nums':nums})

def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'events/add_venue.html', {"form":form, 'submitted':submitted} )

def all_events(request):
    event_list = Event.objects.all().order_by('event_date')
    return render(request, 'events/event_list.html', {'event_list':event_list})



def home(request):
    return render(request, 'events/home.html', {})

