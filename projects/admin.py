from django.contrib import admin

from projects.models import Project

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'desc')
    list_display = ('name', 'link')

    fieldsets = (
        ('Summary', {'fields': ('name', 'desc'),
                     'classes': ('monospace',)}),
        ('Details', {'fields': ('slug', 'link')})
    )

admin.site.register(Project, ProjectAdmin)
