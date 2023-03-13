from django.contrib import admin

from members.models import Members, Achievements, CategoriaMenbers

# Register your models here.
admin.site.register(Members)
admin.site.register(Achievements)
admin.site.register(CategoriaMenbers)