# Proxy models allow you to create a different Python interface for an existing model without changing the database structure.

from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['last_name', 'first_name']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class ActivePersonManager(models.Manager):
    """Custom manager for active persons"""
    def get_queryset(self):
        return super().get_queryset().filter(active=True)

class ActivePerson(Person):
    """Proxy model for active persons only"""
    objects = ActivePersonManager()
    
    class Meta:
        proxy = True
        ordering = ['last_name', 'first_name']
        verbose_name = 'Active Person'
        verbose_name_plural = 'Active Persons'
    
    def send_promotion_email(self):
        """Send promotion email to active person"""
        # Implementation would go here
        print(f"Sending promotion email to {self.email}")

class SeniorPerson(Person):
    """Proxy model for senior persons (age 65+)"""
    class Meta:
        proxy = True
        verbose_name = 'Senior Person'
        verbose_name_plural = 'Senior Persons'
    
    def is_senior(self):
        return self.age >= 65
    
    @classmethod
    def get_seniors(cls):
        return cls.objects.filter(age__gte=65)

# Example usage
active_people = ActivePerson.objects.all()  # Only returns active persons
for person in active_people:
    person.send_promotion_email()  # Method only available on ActivePerson proxy

seniors = SeniorPerson.get_seniors()  # Returns all persons aged 65+
for senior in seniors:
    print(f"{senior} is a senior: {senior.is_senior()}")