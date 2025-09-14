# Purpose: Sets the default name for the reverse relation from a related object back to this model.

class Department(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        default_related_name = 'departments'

class Employee(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

# Note: Now department.employees.all() works instead of department.employee_set.all() 