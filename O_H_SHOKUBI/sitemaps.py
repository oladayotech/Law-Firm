from django.contrib.sitemaps import Sitemap
from .models import News  # replace with your main model

class NewsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return News.objects.all()

    def lastmod(self, obj):
        return obj.creted_time_date  # or obj.created if no updated
