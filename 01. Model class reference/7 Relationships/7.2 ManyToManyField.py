# A ManyToManyField represents a many-to-many relationship, where multiple instances of one model can be related to multiple instances of another model.

from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=10, unique=True)
    enrollment_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"

class Course(models.Model):
    code = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    credits = models.PositiveSmallIntegerField()
    
    # Many-to-many relationship with students through Enrollment
    students = models.ManyToManyField(
        Student,
        through='Enrollment',
        through_fields=('course', 'student'),
        related_name='courses'
    )
    
    def __str__(self):
        return f"{self.code}: {self.title}"

class Enrollment(models.Model):
    """Intermediate model for the many-to-many relationship"""
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    grade = models.CharField(
        max_length=2,
        choices=[
            ('A', 'Excellent'),
            ('B', 'Good'),
            ('C', 'Average'),
            ('D', 'Below Average'),
            ('F', 'Fail'),
            ('W', 'Withdrawn'),
        ],
        null=True,
        blank=True
    )
    
    class Meta:
        unique_together = [['student', 'course']]
    
    def __str__(self):
        return f"{self.student} enrolled in {self.course}"

# Example usage
student = Student.objects.get(pk=1)
course = Course.objects.get(pk=1)

# Enroll student in course with intermediate model
enrollment = Enrollment.objects.create(
    student=student,
    course=course,
    grade=None  # Grade will be assigned later
)

# Query enrollments for a student
student_enrollments = student.enrollment_set.all()
for enrollment in student_enrollments:
    print(f"Course: {enrollment.course}, Grade: {enrollment.grade}")

# Query students in a course
course_students = course.students.all()
for student in course_students:
    print(f"Student: {student}")