from django.contrib import admin
from irbSite.models import Project

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_id', 'project_name', 'user', 'last_modified', 'is_complete', 'is_approved')
    list_filter = ('date_submitted', 'is_complete', 'is_approved', 'user')
    search_fields = ('project_name', 'REVIEW_TYPE')

admin.site.register(Project, ProjectAdmin)
