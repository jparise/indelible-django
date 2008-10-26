from django.db import models
from django.contrib import admin

import tagging
import tagging.fields

class Project(models.Model):
    name = models.CharField(max_length=160)
    slug = models.SlugField(unique=True)
    desc = models.TextField()
    link = models.URLField()
    tags = tagging.fields.TagField()

    class Meta:
        verbose_name_plural = 'Projects'

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return self.link

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'desc')
    list_display = ('name', 'link', 'tags')

    fieldsets = (
        ('Summary', {'fields': ('name', 'desc'),
                     'classes': ('monospace',)}),
        ('Details', {'fields': ('slug', 'link', 'tags')})
    )

admin.site.register(Project, ProjectAdmin)
tagging.register(Project, 'tag_set')
