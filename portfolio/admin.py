from django.contrib import admin
from .models import Project, Skill


# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'display_skills')
    list_filter = ['created_at']
    search_fields = ('title',)

    def display_skills(self, obj):
        return ", ".join([skill.name for skill in obj.skills.all()])

    display_skills.short_description = 'Skills'


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
