from django.contrib import admin

from .models import Skill, Project, ProjectImage, ProjectSkill

# Register your models here.
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(ProjectImage)
admin.site.register(ProjectSkill)