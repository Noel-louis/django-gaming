from django.contrib import admin
from lesJeux.models import Jeux, Studio, Tag


admin.site.register(Jeux)

class JeuxAdmin(admin.ModelAdmin):
    list_display=('nom', 'description', 'studio', 'tags', 'date')

admin.register(Jeux, JeuxAdmin)

admin.site.register(Studio)

class StudiosAdmin(admin.ModelAdmin):
    list_display=('nom', 'description', 'date_creation')

admin.register(Studio, StudiosAdmin)

admin.site.register(Tag)

class TagsAdmin(admin.ModelAdmin):
    list_display=('nom', 'description')

admin.register(Tag, TagsAdmin)