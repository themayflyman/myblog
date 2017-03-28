from django.contrib import admin
from .import models
from markdownx.admin import MarkdownxModelAdmin


class EntryAdmin(MarkdownxModelAdmin):
    list_display = ("title", "created")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(models.Entry, EntryAdmin)
admin.site.register(models.Comment)
admin.site.register(models.Tag)