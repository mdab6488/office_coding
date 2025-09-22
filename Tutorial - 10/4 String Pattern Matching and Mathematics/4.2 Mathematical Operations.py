# Python provides several modules for mathematical operations that are useful for web applications dealing with analytics, data processing, or scientific computations.

"""4.2.1 Basic Math Operations"""
import math

# Calculate distance between two points (for location-based services)
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Pagination calculations
total_items = 103
items_per_page = 10
total_pages = math.ceil(total_items / items_per_page)
print(f"Total pages needed: {total_pages}")

# Logarithmic scale for analytics visualization
values = [10, 100, 1000, 10000]
log_values = [math.log10(x) for x in values]
print(f"Log values: {log_values}")

"""4.2.2 Random Number Generation"""
import random

# Generate random tokens for CSRF protection or password reset
def generate_token(length=32):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(characters) for _ in range(length))

# Random sampling for A/B testing
users = ['user1', 'user2', 'user3', 'user4', 'user5']
test_group = random.sample(users, 2)
print(f"Test group: {test_group}")

# Shuffle content for varied user experience
content_list = ['item1', 'item2', 'item3', 'item4', 'item5']
random.shuffle(content_list)
print(f"Shuffled content: {content_list}")

"""4.2.3 Statistical Calculations"""
import statistics

# Analyze response times for performance monitoring
response_times = [12.5, 13.2, 11.8, 15.3, 12.1, 14.5, 12.8]
mean_time = statistics.mean(response_times)
median_time = statistics.median(response_times)
stdev_time = statistics.stdev(response_times)

print(f"Mean response time: {mean_time:.2f}ms")
print(f"Median response time: {median_time:.2f}ms")
print(f"Standard deviation: {stdev_time:.2f}ms")

# Identify outliers in user behavior metrics
data = [120, 125, 118, 153, 121, 145, 128, 450]  # last one might be outlier
try:
    clean_data = statistics.filter_outliers(data)
except AttributeError:
    # Fallback for versions without filter_outliers
    mean = statistics.mean(data)
    stdev = statistics.stdev(data)
    clean_data = [x for x in data if mean - 2 * stdev < x < mean + 2 * stdev]

print(f"Original data: {data}")
print(f"Cleaned data: {clean_data}")

# These mathematical capabilities are essential for web applications that need to process data, perform analytical computations, or generate randomized content for users 