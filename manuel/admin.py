from django.contrib import admin
from manuel.models import Planet


class PlanetAdmin(admin.ModelAdmin):
    pass

admin.site.register(Planet, PlanetAdmin)
