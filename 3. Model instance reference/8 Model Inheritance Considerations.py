# When working with model inheritance, instance methods behave differently:

class BaseArticle(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

class FeaturedArticle(BaseArticle):
    featured_image = models.ImageField(upload_to='articles/')
    highlight = models.BooleanField(default=False)

# Creating instances
featured_article = FeaturedArticle.objects.create(
    title="Featured",
    featured_image="image.jpg",
    highlight=True
)

# The save method works for both base and child models
featured_article.save()

# Refresh from database works for all fields
featured_article.refresh_from_db()