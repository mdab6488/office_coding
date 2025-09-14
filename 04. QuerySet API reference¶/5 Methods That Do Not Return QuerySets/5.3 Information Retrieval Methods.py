# in_bulk() - Retrieves objects by ID as a dictionary
books_dict = Book.objects.in_bulk([1, 2, 3])  # Returns {1: <Book>, 2: <Book>, ...} :cite[4]

# first() and last() - Get the first/last object from QuerySet
first_book = Book.objects.first()  # First book by ordering :cite[4]
last_book = Book.objects.last()   # Last book by ordering :cite[4]

# earliest() and latest() - Get objects by date fields
recent_book = Book.objects.earliest('published_date')  # Earliest publication
oldest_book = Book.objects.latest('published_date')    # Latest publication :cite[4]

# aggregate() - Perform aggregation across the entire QuerySet
from django.db.models import Avg, Max, Min
stats = Book.objects.aggregate(
    avg_price=Avg('price'),
    max_price=Max('price'),
    min_price=Min('price')
)  # Returns: {'avg_price': 85.5, 'max_price': 200, 'min_price': 10} :cite[4]

# exists() - Check if any objects exist
has_books = Book.objects.exists()  # Returns True or False :cite[4]

# count() - Get the number of objects
book_count = Book.objects.count()  # Returns integer count :cite[4]

# explanation() - Get query execution plan
explanation = Book.objects.filter(price__gt=100).explain()  # Query execution plan :cite[4]