# The re module provides comprehensive regular expression support, essential for web applications that need to validate user input, extract information from text, or process content.

import re

# Validate email format (simplified version)
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

# Extract all URLs from text (useful for content processing)
def extract_urls(text):
    pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[/\w\.-]*\??[/\w\.-=&%]*'
    return re.findall(pattern, text)

# Simple HTML tag stripping (for content previews)
def strip_html_tags(html):
    return re.sub(r'<[^>]+>', '', html)

# Example usage
sample_text = "Contact us at info@example.com or visit https://example.com"
print(f"Email valid: {validate_email('info@example.com')}")
print(f"URLs found: {extract_urls(sample_text)}")

# Replace multiple spaces with single spaces (clean user input)
user_input = "This  has   too    many spaces"
cleaned = re.sub(r'\s+', ' ', user_input)
print(f"Cleaned input: {cleaned}")

# For simpler string operations, Python's built-in string methods are often more appropriate and readable 
# Simple replacement is often better with string methods
message = 'tea for too'
fixed_message = message.replace('too', 'two')
print(fixed_message)  # Output: 'tea for two'