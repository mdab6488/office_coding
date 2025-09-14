# Django provides several methods to validate model data before it's saved to the database. The most important are clean() and full_clean().

from django.db import models
from django.core.exceptions import ValidationError

class Reservation(models.Model):
    customer_name = models.CharField(max_length=100)
    check_in = models.DateField()
    check_out = models.DateField()
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    
    def clean(self):
        """Custom validation for the reservation"""
        super().clean()
        
        # Check that check_out is after check_in
        if self.check_out <= self.check_in:
            raise ValidationError({
                'check_out': 'Check-out date must be after check-in date.'
            })
        
        # Check for overlapping reservations
        overlapping = Reservation.objects.filter(
            room=self.room,
            check_in__lt=self.check_out,
            check_out__gt=self.check_in
        ).exclude(id=self.id)  # Exclude current instance when updating
        
        if overlapping.exists():
            raise ValidationError({
                'room': 'This room is already reserved for the selected dates.'
            })
    
    def save(self, *args, **kwargs):
        # Run full validation before saving
        self.full_clean()
        super().save(*args, **kwargs)

# Example usage
try:
    reservation = Reservation(
        customer_name="John Doe",
        check_in="2023-12-01",
        check_out="2023-11-30",  # Invalid: check_out before check_in
        room=Room.objects.first()
    )
    reservation.save()  # This will raise a ValidationError
except ValidationError as e:
    print(f"Validation error: {e.message_dict}")