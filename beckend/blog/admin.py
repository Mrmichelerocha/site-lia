from django.contrib import admin

from blog.models import Blog
from blog.models import CategoriaBlog

# Register your models here.
admin.site.register(Blog)
admin.site.register(CategoriaBlog)