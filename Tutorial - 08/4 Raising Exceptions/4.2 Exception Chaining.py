# Python allows you to chain exceptions using the from keyword, which preserves the original exception context, making debugging easier.

# Example 1: Explicit exception chaining
def load_configuration(config_file):
    try:
        with open(config_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError as e:
        raise ConfigurationError(f"Config file {config_file} not found") from e
    except json.JSONDecodeError as e:
        raise ConfigurationError(f"Invalid JSON in {config_file}") from e

# Example 2: Handling exceptions with implicit chaining
def load_user_data(user_id):
    try:
        with database_connection() as conn:
            return conn.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    except DatabaseError as e:
        # __context__ is automatically set to the caught exception
        raise DataLoadError("Failed to load user data") from e

# Example 3: Using from None to suppress exception context
def safe_parse_int(value, default=0):
    try:
        return int(value)
    except (TypeError, ValueError):
        # Suppress the original exception context
        raise ValueError(f"Invalid integer value: {value}") from None