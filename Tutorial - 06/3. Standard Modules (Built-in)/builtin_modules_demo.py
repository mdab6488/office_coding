import os
import sys
import json
import urllib.parse
from datetime import datetime

# File paths
current_dir = os.path.dirname(__file__)
template_path = os.path.join(current_dir, 'templates', 'index.html')
print(f"Template path: {template_path}")

# JSON API response
api_response = {
    "status": "success",
    "data": {"user": "john_doe", "id": 123},
    "timestamp": datetime.now().isoformat()
}
print(json.dumps(api_response))

# URL parsing
parsed_url = urllib.parse.urlparse('https://example.com/path?query=string')
print(f"Scheme: {parsed_url.scheme}")
print(f"Netloc: {parsed_url.netloc}")
