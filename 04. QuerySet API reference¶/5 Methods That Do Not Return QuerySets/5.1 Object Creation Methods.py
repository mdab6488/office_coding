# create() - Creates and saves an object in one step
new_author = Author.objects.create(name="New Author", age=40)  :cite[4]

# get_or_create() - Gets an object or creates it if it doesn't exist
author, created = Author.objects.get_or_create(
    name="John Doe",
    defaults={'age': 30, 'email': 'john@example.com'}
)  # Returns (object, created_flag)

# update_or_create() - Updates an object or creates it if it doesn't exist
author, created = Author.objects.update_or_create(
    name="John Doe",
    defaults={'age': 35, 'email': 'john.doe@example.com'}  # Values to update/create
)  # Returns (object, created_flag)

# bulk_create() - Creates multiple objects in a single query
authors = [
    Author(name="Author 1", age=40),
    Author(name="Author 2", age=45),
    Author(name="Author 3", age=50)
]
Author.objects.bulk_create(authors)  # Efficient mass creation :cite[4]

# bulk_update() - Updates multiple objects in a single query
authors = Author.objects.all()
for author in authors:
    author.age += 1  # Increment each author's age
Author.objects.bulk_update(authors, ['age'])  # Update only the age field :cite[4]