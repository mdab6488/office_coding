"""
A collection of utilities for web development.
"""
import requests
from urllib.parse import urlparse

def validate_url(url):
    """Check if a URL is properly formatted."""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def fetch_json(url):
    """Fetch JSON data from a URL."""
    if not validate_url(url):
        raise ValueError("Invalid URL")
    
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    # Test code that runs only when executed directly
    test_url = "https://httpbin.org/json"
    print(f"Testing URL: {test_url}")
    print(f"URL valid: {validate_url(test_url)}")
    
    try:
        data = fetch_json(test_url)
        print("Successfully fetched JSON data")
        print(f"Title: {data['slideshow']['title']}")
    except Exception as e:
        print(f"Error: {e}")

"""Run with:"""
# python web_utils.py
