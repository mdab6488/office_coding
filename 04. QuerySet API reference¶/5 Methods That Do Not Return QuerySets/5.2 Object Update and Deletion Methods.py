# update() - Updates all objects in the QuerySet
Book.objects.filter(price__lt=100).update(price=120)  # Set price to 120 for all books under 100 :cite[4]

# delete() - Deletes all objects in the QuerySet
Book.objects.filter(price__gt=1000).delete()  # Deletes expensive books :cite[4]

# Saving individual objects
book = Book.objects.get(id=1)
book.price = 150
book.save()  # Saves changes to this specific object :cite[2]

# Saving with update_fields (optimization)
book.save(update_fields=['price'])  # Only update the price field

# Related object management with add(), remove(), set()
author = Author.objects.get(name="J.K. Rowling")
book = Book.objects.get(title="Harry Potter 1")

# Many-to-many relationship management
book.authors.add(author)  # Add author to book's authors :cite[2]
book.authors.remove(author)  # Remove author from book's authors
book.authors.set([author1, author2])  # Set exactly these authors