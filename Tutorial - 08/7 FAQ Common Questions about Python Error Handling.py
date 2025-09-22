# Q: Should I catch all exceptions in my web application?
# A: No, you shouldn't catch all exceptions indiscriminately. Catch specific exceptions you can handle meaningfully, and let others propagate to a general error handler that can log them and display a generic error page to the user

# Q: How can I log exceptions effectively?
# A: Use Python's logging module to capture exception information with tracebacks:
try:
    process_request()
except Exception as e:
    logger.exception("Unhandled exception occurred")  # Automatically includes traceback
    raise  # Re-raise after logging

# Q: When should I create custom exception classes?
# A: Create custom exceptions when you need to communicate specific error conditions that built-in exceptions don't adequately represent. This is especially useful for domain-specific errors in your application.

# Q: How should I handle validation errors in web forms?
# A: For form validation, collect all validation errors and present them together rather than failing on the first error. Use exception hierarchies specifically for validation:
class ValidationError(Exception):
    def __init__(self, errors):
        self.errors = errors  # Dictionary of field -> error messages

def validate_registration_form(data):
    errors = {}
    if not data.get('username'):
        errors['username'] = 'Username is required'
    if len(data.get('password', '')) < 8:
        errors['password'] = 'Password must be at least 8 characters'
    if errors:
        raise ValidationError(errors)

