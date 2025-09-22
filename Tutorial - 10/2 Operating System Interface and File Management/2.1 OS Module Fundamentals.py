# The os module provides a unified interface for interacting with the operating system, allowing Python code to remain portable across different platforms. For web development, this is particularly useful for file system operations and environment configuration.

import os

# Get current working directory
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# Change working directory (useful for accessing application files)
os.chdir('/server/accesslogs')

# Create a new directory (e.g., for user uploads)
os.system('mkdir user_uploads')

# Better alternative to system calls for directory creation
os.makedirs('user_uploads/images', exist_ok=True)

# Get environment variables (e.g., for configuration)
database_url = os.environ.get('DATABASE_URL')
if not database_url:
    print("DATABASE_URL not set")

# It's important to use import os rather than from os import * to avoid namespace collisions, particularly with the built-in open() function, which behaves differently from os.open() 