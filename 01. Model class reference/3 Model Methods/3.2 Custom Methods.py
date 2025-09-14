# Adding custom methods to your models encapsulates business logic within the model, keeping your code organized and following the "fat models, thin views" principle.

from django.db import models
from django.utils import timezone

class Event(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    capacity = models.PositiveIntegerField()
    attendees = models.ManyToManyField('Attendee', through='Registration')
    
    def is_upcoming(self):
        """Check if the event is in the future"""
        return self.start_date > timezone.now()
    
    def is_full(self):
        """Check if event has reached capacity"""
        return self.registrations.count() >= self.capacity
    
    def duration(self):
        """Calculate the duration of the event in hours"""
        if self.end_date and self.start_date:
            duration = self.end_date - self.start_date
            return duration.total_seconds() / 3600  # Convert to hours
        return 0
    
    def get_absolute_url(self):
        """Generate canonical URL for the event"""
        from django.urls import reverse
        return reverse('event_detail', kwargs={'pk': self.pk})

# Example usage
event = Event.objects.get(pk=1)
print(f"Is upcoming: {event.is_upcoming()}")
print(f"Is full: {event.is_full()}")
print(f"Duration: {event.duration()} hours")
print(f"URL: {event.get_absolute_url()}")