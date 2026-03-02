from django.contrib import admin
from .models import Skill, SkillCategory

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display  = ['name', 'category', 'level', 'order']
    list_editable = ['level', 'order']
    list_filter   = ['category']