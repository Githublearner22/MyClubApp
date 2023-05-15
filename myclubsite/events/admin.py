from django.contrib import admin
from .models import Venue
from .models import MyUser #MyUser not My Club User
from .models import Event

#admin.site.register(Venue)
admin.site.register(MyUser)
#admin.site.register(Event)

#This allows to make changes to adming for 
@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    ordering = ('name',)
    search_fields = ('name', 'address')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('name', 'venue'), 'event_date', 'description', 'manager')
    list_display = ('name', 'event_date', 'venue')
    list_filter = ('event_date', 'venue')
    ordering = ('-event_date',)