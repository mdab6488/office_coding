# String lookups provide pattern matching capabilities for text fields:

# Case-sensitive contains
Product.objects.filter(name__contains="apple")

# Case-insensitive contains
Product.objects.filter(name__icontains="apple")

# Starts with
Product.objects.filter(name__startswith="Pro")

# Case-insensitive starts with
Product.objects.filter(name__istartswith="pro")

# Ends with
Product.objects.filter(name__endswith="Phone")

# Case-insensitive ends with
Product.objects.filter(name__iendswith="phone")

# These lookups are invaluable for search functionality and text-based filtering. The icontains lookup is particularly useful for implementing search features where case sensitivity shouldn't affect results