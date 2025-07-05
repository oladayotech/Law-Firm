from django.db import models
from django.utils.text import slugify

from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage

class CloudinaryImageField(models.ImageField):
    def __init__(self, *args, **kwargs):
        kwargs['storage'] = MediaCloudinaryStorage()
        super().__init__(*args, **kwargs)


# Create your models here.
class News(models.Model):
    """Model for News."""

    headline = models.CharField(max_length=255)
    headline_for_url = models.SlugField(max_length=255, blank=True)
    news_images = CloudinaryImageField(upload_to='news/', null=True, blank=True)
    news_body = models.TextField(blank=True)
    created_time_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.headline} - {self.created_time_date.date()}"

    def save(self, *args, **kwargs):
        # Automatically generate slug from headline
        if not self.headline_for_url:
            self.headline_for_url = slugify(self.headline)
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('news_detail', kwargs={'slug': self.headline_for_url})
        
class Lawyer(models.Model):
    name = models.CharField(max_length=200)
    name_for_url = models.SlugField(max_length=200, blank=True)
    title = models.CharField(max_length=100)  # e.g. 'Managing Partner', 'Senior Associate'
    photo = CloudinaryImageField(upload_to='lawyers/', blank=True, null=True)
    bio = models.TextField(blank=True)
    education = models.TextField(blank=True)
    practice_area = models.CharField(max_length=200, blank=True)
    linkedin = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    # Add other fields if needed

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Automatically generate slug from name
        if not self.name_for_url:
            self.name_for_url = slugify(self.name)
        super().save(*args, **kwargs)
        
from cloudinary_storage.storage import MediaCloudinaryStorage

class Practice(models.Model):
    practice_name = models.CharField(max_length=200)
    practice_name_for_url = models.SlugField(max_length=200, blank=True)
    practice_info = models.TextField(blank=True)
    practice_image = models.ImageField(blank=True, upload_to='practice/', storage=MediaCloudinaryStorage())
    practice_expertise_raw = models.TextField(
        blank=True,
        help_text="Separate each item with a new line"
    )
    lawyers = models.ManyToManyField(Lawyer, blank=True)  #  correct M2M relationship
    
    def get_expertise_list(self):
        return [item.strip() for item in self.practice_expertise_raw.split('\n') if item.strip()]

    class Meta:
        verbose_name = 'Practice'
        verbose_name_plural = 'Practices'

    def __str__(self):
        return self.practice_name

    def save(self, *args, **kwargs):
        print(">>> Saving Practice")
        print(">>> File storage:", self.practice_image.storage)
        if not self.practice_name_for_url:
            self.practice_name_for_url = slugify(self.practice_name)
        super().save(*args, **kwargs)