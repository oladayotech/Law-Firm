from django.db import models
from django.utils.text import slugify


# Create your models here.
class News(models.Model):
    """Model for News."""

    headline = models.CharField(max_length=255)
    headline_for_url = models.SlugField(max_length=255, blank=True)
    news_images = models.ImageField(upload_to='news/', null=True, blank=True)
    news_body = models.TextField(blank=True)
    created_time_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.headline} - {self.created_time_date.date()}"

    def save(self, *args, **kwargs):
        # Automatically generate slug from headline
        if not self.headline_for_url:
            self.headline_for_url = slugify(self.headline)
        super().save(*args, **kwargs)

