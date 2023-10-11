from django.contrib import admin
from lesJeux.models import Jeux


admin.site.register(Jeux)

class JeuxAdmin(admin.ModelAdmin):
    list_display=('nom', 'description', 'studio', 'tags', 'date')

admin.register(Jeux, JeuxAdmin)