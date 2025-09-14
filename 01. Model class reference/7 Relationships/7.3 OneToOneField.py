# A OneToOneField represents a one-to-one relationship, where each instance of one model is related to exactly one instance of another model.

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """Extends the built-in User model with additional fields"""
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        primary_key=True,  # Makes this a one-to-one relationship
        related_name='profile'
    )
    bio = models.TextField(blank=True, help_text="Tell us about yourself")
    date_of_birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    
    # Social media links
    twitter = models.URLField(blank=True, help_text="Your Twitter profile URL")
    linkedin = models.URLField(blank=True, help_text="Your LinkedIn profile URL")
    github = models.URLField(blank=True, help_text="Your GitHub profile URL")
    
    # Preferences
    email_notifications = models.BooleanField(default=True)
    newsletter_subscription = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Profile of {self.user.username}"

class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    founded_date = models.DateField(null=True, blank=True)
    website = models.URLField(blank=True)
    
    def __str__(self):
        return self.name

class CompanyProfile(models.Model):
    """Additional details for a company"""
    company = models.OneToOneField(
        Company,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    employees = models.PositiveIntegerField(null=True, blank=True)
    revenue = models.DecimalField(
        max_digits=15, 
        decimal_places=2, 
        null=True, 
        blank=True,
        help_text="Annual revenue in USD"
    )
    headquarters = models.CharField(max_length=200, blank=True)
    industries = models.ManyToManyField('Industry', related_name='companies')
    
    def __str__(self):
        return f"Profile of {self.company.name}"

class Industry(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

# Example usage
user = User.objects.get(username='johndoe')
profile, created = UserProfile.objects.get_or_create(
    user=user,
    defaults={
        'bio': 'Software developer and open source enthusiast',
        'phone': '+1234567890',
    }
)

# Update profile
profile.twitter = 'https://twitter.com/johndoe'
profile.save()

# Access profile from user
user_profile = user.profile
print(user_profile.bio)

# Company example
company = Company.objects.create(
    name="Tech Innovations Inc.",
    description="A company focused on innovative technology solutions",
    founded_date="2010-05-15",
    website="https://techinnovations.example.com"
)

company_profile = CompanyProfile.objects.create(
    company=company,
    employees=250,
    revenue=50000000.00,
    headquarters="San Francisco, CA"
)

# Add industries
software = Industry.objects.get_or_create(name="Software")[0]
consulting = Industry.objects.get_or_create(name="Consulting")[0]
company_profile.industries.add(software, consulting)