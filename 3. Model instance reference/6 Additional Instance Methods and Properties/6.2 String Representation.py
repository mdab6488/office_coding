# It's good practice to define the __str__() method for your models:

class Article(models.Model):
    # ... fields as above ...
    
    def __str__(self):
        return self.title

# Usage
article = Article(title="My Article")
print(str(article))  # Output: "My Article"