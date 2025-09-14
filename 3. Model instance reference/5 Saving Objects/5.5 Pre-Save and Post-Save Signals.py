# In addition to overriding the save method, you can use signals to add behavior around saving:

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

@receiver(pre_save, sender=Article)
def article_pre_save(sender, instance, **kwargs):
    """Signal receiver before an Article is saved"""
    print(f"About to save article: {instance.title}")

@receiver(post_save, sender=Article)
def article_post_save(sender, instance, created, **kwargs):
    """Signal receiver after an Article is saved"""
    if created:
        print(f"Created new article: {instance.title}")
    else:
        print(f"Updated article: {instance.title}")

# Connect the signals (usually done in apps.py or models.py)