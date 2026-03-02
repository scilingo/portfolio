from django.contrib import admin
from .models import Education, Experience

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display  = ['institution', 'degree', 'start_date', 'in_progress']
    list_editable = ['in_progress']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display  = ['organization', 'role', 'type', 'start_date', 'current']
    list_editable = ['current']
    list_filter   = ['type']