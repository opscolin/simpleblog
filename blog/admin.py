from django.contrib import admin
from .models import Tag, Category, Blog

# Register your models here.
admin.site.register([Category, Tag, Blog])

