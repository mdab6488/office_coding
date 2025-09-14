# The all() method returns a QuerySet containing all records in the model's database table. This is the most basic way to retrieve all objects from a model.

# Get all members
members = Member.objects.all()

# Get all books
books = Book.objects.all()

# The returned QuerySet is lazy and doesn't hit the database until evaluated . You can use it in templates to iterate through all objects or chain it with other methods for filtering.

