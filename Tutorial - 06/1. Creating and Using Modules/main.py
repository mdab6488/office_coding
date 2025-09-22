"""
Main application using our web_utils module.
"""
import web_utils  # Import the entire module
from web_utils import validate_url  # Import specific function
from web_utils import fetch_json as get_json  # Import with alias

url = "https://api.github.com/users/python"

# Using the module
if web_utils.validate_url(url):
    data = web_utils.fetch_json(url)
    print(f"GitHub user: {data['login']}")

# Using the specifically imported function
if validate_url(url):
    data = get_json(url)
    print(f"GitHub user: {data['login']}")
