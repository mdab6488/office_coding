# The datetime module provides comprehensive tools for working with dates and times, which is essential for web applications that need to handle scheduling, content publication, or user activity tracking.

from datetime import datetime, date, timedelta
import time

# Get current date and time
now = datetime.now()
print(f"Current datetime: {now}")

# Format dates for display on websites
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted datetime: {formatted_date}")

# Calculate time differences (e.g., for user session management)
last_activity = datetime(2023, 10, 15, 14, 30, 0)
time_since_activity = now - last_activity
print(f"Time since last activity: {time_since_activity}")

# Check if content should be published based on publication date
publication_date = date(2023, 10, 20)
current_date = date.today()
if current_date >= publication_date:
    print("Content should be published")
else:
    print("Content not yet scheduled for publication")

# Add time to current date (e.g., for subscription expiration)
one_month_later = now + timedelta(days=30)
print(f"Subscription expires: {one_month_later}")