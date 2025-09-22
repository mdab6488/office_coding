# The else clause in exception handling runs only when no exception occurred in the try block, while the finally clause always executes, making it ideal for cleanup operations.

# Example 1: Database transaction with else and finally
try:
    db.start_transaction()
    user = create_user(request.POST)
    profile = create_profile(user, request.POST)
except ValidationError as e:
    db.rollback()
    return render(request, 'error.html', {'error': e})
else:
    # Only commit if no exceptions occurred
    db.commit()
    return redirect('user_dashboard')
finally:
    # Always release the database connection
    db.release_connection()

# Example 2: File operations with else and finally
try:
    log_file = open('app.log', 'a')
    log_data = generate_log_data()
except IOError as e:
    print(f"Failed to open log file: {e}")
else:
    # Only write to the file if it was successfully opened
    log_file.write(log_data)
finally:
    # Ensure the file is closed even if write operation fails
    if 'log_file' in locals() and not log_file.closed:
        log_file.close()