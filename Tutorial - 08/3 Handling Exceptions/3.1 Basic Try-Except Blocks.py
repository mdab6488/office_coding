# The try statement allows you to define code blocks that might raise exceptions, along with handlers that specify how to respond to those exceptions.

# Example 1: Handling specific exceptions
try:
    user_id = int(request.GET['user_id'])  # Might raise ValueError or KeyError
    user = User.objects.get(id=user_id)  # Might raise DoesNotExist exception
except ValueError:
    return HttpResponse("Invalid user ID format", status=400)
except KeyError:
    return HttpResponse("User ID parameter missing", status=400)
except User.DoesNotExist:
    return HttpResponse("User not found", status=404)

# Example 2: Handling multiple exceptions in a single clause
try:
    file = open('config.json', 'r')
    config_data = json.load(file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Configuration error: {e}")
    # Fall back to default configuration
    config_data = DEFAULT_CONFIG

# Example 3: Using the else clause for code that should only run if no exception occurred
try:
    connection = database.connect()
except DatabaseError as e:
    print(f"Database connection failed: {e}")
else:
    # This code only runs if no exception was raised
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    connection.close()

# Example 4: Using the finally clause for cleanup operations
file = None
try:
    file = open('important_data.txt', 'r')
    process_file(file)
except IOError as e:
    print(f"File error: {e}")
finally:
    # This code always runs, whether an exception occurred or not
    if file is not None:
        file.close()  # Ensure file is always closed