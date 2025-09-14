# Multi-table inheritance creates a separate database table for each model in the inheritance hierarchy, with each table containing only the fields defined in that specific model.

from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    
    class Meta:
        ordering = ['last_name', 'first_name']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Employee(Person):
    employee_id = models.CharField(max_length=10, unique=True)
    hire_date = models.DateField()
    department = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    
    def years_of_service(self):
        """Calculate years of service"""
        from datetime import date
        today = date.today()
        return today.year - self.hire_date.year - (
            (today.month, today.day) < (self.hire_date.month, self.hire_date.day)
        )

class Customer(Person):
    customer_since = models.DateField()
    loyalty_points = models.PositiveIntegerField(default=0)
    preferred_customer = models.BooleanField(default=False)
    
    def add_loyalty_points(self, points):
        """Add loyalty points to customer"""
        self.loyalty_points += points
        if self.loyalty_points > 1000:
            self.preferred_customer = True
        self.save()

# Example usage
employee = Employee.objects.create(
    first_name="Alice",
    last_name="Smith",
    date_of_birth="1990-05-15",
    employee_id="EMP12345",
    hire_date="2018-03-10",
    department="Engineering",
    salary=75000.00
)

print(employee)  # Output: "Alice Smith" (inherited from Person)
print(employee.years_of_service())  # Calls Employee method

customer = Customer.objects.create(
    first_name="Bob",
    last_name="Johnson",
    date_of_birth="1985-11-22",
    customer_since="2020-01-15",
    loyalty_points=500
)

customer.add_loyalty_points(600)  # Now has 1100 points, becomes preferred customer
print(customer.preferred_customer)  # Output: True