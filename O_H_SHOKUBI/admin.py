from django.contrib import admin

from . import models
# from models import News

# Register your models here.
admin.site.register(models.News)
admin.site.register(models.Lawyer)
admin.site.register(models.Practice)