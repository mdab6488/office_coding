# JSON Handling: Web APIs often use JSON. Use Python's json module:
import json
data = {'name': 'Alice', 'age': 30}
json_output = json.dumps(data)  # Convert to JSON string
print(json_output)  # Output: {"name": "Alice", "age": 30}

# Environment Variables: For configuration, use os.environ:
import os
db_url = os.environ.get('DATABASE_URL', 'default_url')
print(f"Database URL: {db_url}")

