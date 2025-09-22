"""Be Specific in Exception Handling: Catch the most specific exception types first, then more general ones."""
# Good practice: specific exceptions first
try:
    process_user_data()
except ValidationError as e:
    handle_validation_error(e)
except DatabaseError as e:
    handle_database_error(e)
except Exception as e:
    handle_unexpected_error(e)  # General catch-all
    
# Bad practice: catching everything generically
try:
    process_user_data()
except Exception as e:  # Too broad
    handle_error(e)
    
"""Don't Suppress Exceptions Silently: Avoid using bare except clauses without logging or handling the exception."""
    
# Bad practice: silent failure
try:
    save_user_data()
except:
    pass  # This will hide all errors
    
# Good practice: proper logging
try:
    save_user_data()
except DatabaseError as e:
    logger.error("Failed to save user data: %s", e)
    raise  # Re-raise after logging

"""Use Finally for Cleanup: Ensure resources are properly released using finally blocks."""
# Ensure database connection is closed
connection = None
try:
    connection = database.connect()
    # Perform operations
except DatabaseError as e:
    logger.error("Database operation failed: %s", e)
finally:
    if connection is not None:
        connection.close()  # Always executed