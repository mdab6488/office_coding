# For complex web applications, creating custom exception classes can make your error handling more precise and expressive.

# Example 1: Basic custom exception
class WebAppError(Exception):
    """Base exception for our web application"""
    pass

# Example 2: Custom exception with additional attributes
class ValidationError(WebAppError):
    """Raised when data validation fails"""
    
    def __init__(self, message, field=None, value=None):
        super().__init__(message)
        self.field = field
        self.value = value
    
    def to_dict(self):
        """Convert exception to dictionary for JSON responses"""
        error_data = {'message': str(self)}
        if self.field is not None:
            error_data['field'] = self.field
        if self.value is not None:
            error_data['value'] = self.value
        return error_data

# Example 3: Hierarchy of custom exceptions
class DatabaseError(WebAppError):
    """Base exception for database-related errors"""
    pass

class ConnectionError(DatabaseError):
    """Raised when database connection fails"""
    pass

class QueryError(DatabaseError):
    """Raised when a database query fails"""
    
    def __init__(self, message, query=None, params=None):
        super().__init__(message)
        self.query = query
        self.params = params

# Using the custom exceptions
def execute_query(query, params=None):
    try:
        with db.cursor() as cursor:
            cursor.execute(query, params or [])
            return cursor.fetchall()
    except db.DatabaseError as e:
        # Wrap the underlying database error
        raise QueryError(f"Query failed: {e}", query, params) from e