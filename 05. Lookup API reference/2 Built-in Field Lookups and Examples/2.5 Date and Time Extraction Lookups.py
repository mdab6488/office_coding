# Temporal lookups provide access to specific components of date and time fields:

# Year lookup
Order.objects.filter(order_date__year=2023)

# Month lookup
Order.objects.filter(order_date__month=12)  # December

# Day lookup
Order.objects.filter(order_date__day=25)    # 25th of month

# Week lookups
Order.objects.filter(order_date__week=52)   # 52nd week
Order.objects.filter(order_date__week_day=2)  # Tuesday (1=Sunday, 2=Monday)
Order.objects.filter(order_date__iso_week_day=2)  # Monday (ISO: 1=Monday)

# Time-based lookups
LogEntry.objects.filter(timestamp__hour=14)    # 2 PM
LogEntry.objects.filter(timestamp__minute=30)  # 30 minutes past
LogEntry.objects.filter(timestamp__second=0)   # Exactly on the minute

# These lookups enable temporal analysis of data, such as finding all orders placed in December or log entries occurring at a specific hour.

