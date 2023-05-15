from django import forms
from django.forms import ModelForm
from .models import Venue, Event

#Create a venue form
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'post_code', 'phone', 'website', 'email_address')
        labels = {
            'name':'',
            'address': '',
            'post_code': '',
            'phone': '',
            'website': '',
            'email_address': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Venue Name'}),
            'address': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Address'}),
            'post_code': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Postcode'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Phone Number'}),
            'website': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Website'}),
            'email_address': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email Address'}),
        }

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'event_date', 'venue', 'manager', 'description', 'attendees')
        labels = {
            'name':'',
            'event_date': 'YYYY-MM-DD HH:MM:SS',
            'venue': 'Venue',
            'manager': 'Manager',
            'description': '',
            'attendees':'Attendees',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Event Name'}),
            'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Event Date'}),
            'venue': forms.Select(attrs={'class':'form-select', 'placeholder': 'Venue'}),
            'manager': forms.Select(attrs={'class':'form-select', 'placeholder': 'Manager'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Description'}),
            'attendees': forms.SelectMultiple(attrs={'class':'form-select', 'placeholder': 'Attendees'})
        }
