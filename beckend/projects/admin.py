from django.contrib import admin

from projects.models import Project
from projects.models import CategoriaProjects

# Register your models here.
admin.site.register(Project)
admin.site.register(CategoriaProjects)