# Field options allow you to customize the behavior of your model fields.

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Course(models.Model):
    # Field with multiple options
    title = models.CharField(
        max_length=200,
        verbose_name="Course Title",
        help_text="Enter the title of the course",
        db_index=True  # Create database index for this field
    )
    
    code = models.SlugField(
        max_length=20,
        unique=True,
        verbose_name="Course Code",
        help_text="Unique identifier for the course (e.g., CS101)"
    )
    
    description = models.TextField(
        blank=True,
        verbose_name="Course Description",
        help_text="Detailed description of the course content"
    )
    
    credits = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(6)],
        verbose_name="Credit Hours",
        help_text="Number of credit hours (1-6)"
    )
    
    is_offered = models.BooleanField(
        default=True,
        verbose_name="Currently Offered",
        help_text="Check if the course is currently being offered"
    )
    
    start_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Start Date",
        help_text="Date when the course starts"
    )
    
    end_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="End Date",
        help_text="Date when the course ends"
    )
    
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Course Price",
        help_text="Price of the course in USD"
    )
    
    # Choices with display values
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    
    level = models.CharField(
        max_length=15,
        choices=LEVEL_CHOICES,
        default='beginner',
        verbose_name="Difficulty Level",
        help_text="Select the difficulty level of the course"
    )
    
    class Meta:
        ordering = ['code', 'title']
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        indexes = [
            models.Index(fields=['is_offered', 'level']),
        ]
    
    def __str__(self):
        return f"{self.code}: {self.title}"

# Example usage
course = Course.objects.create(
    title="Introduction to Python Programming",
    code="PY101",
    description="Learn the fundamentals of Python programming language",
    credits=3,
    is_offered=True,
    start_date="2023-09-01",
    end_date="2023-12-15",
    price=299.99,
    level="beginner"
)

print(course)  # Output: "PY101: Introduction to Python Programming"

# Table: Common Field Options and Their Purposes
"""
Field Option	Description	Example
null	If True, allows NULL values in database	null=True
blank	If True, allows empty values in forms	blank=True
choices	Limits field choices to specified values	choices=[('a', 'A'), ('b', 'B')]
default	Default value when no value is provided	default='draft'
help_text	Help text for forms	help_text='Enter your name'
primary_key	Designates field as primary key	primary_key=True
unique	Requires field values to be unique	unique=True
verbose_name	Human-readable name	verbose_name='Publication Date'
validators	Custom validators for the field	validators=[MinValueValidator(0)]
"""
