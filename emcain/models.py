from django.db import models

class Entry(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        abstract=True


class Skill(Entry):
    icon_url = models.URLField()

    def get_projects(self):
        projects = []
        for ps in ProjectSkill.objects.filter(skill=self):
            projects.append(ps.project)
        return projects

class Project(Entry):
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # display null as ongoing
    is_demo = models.BooleanField(default=False)

    def get_skills(self):
        skills = []
        for ps in ProjectSkill.objects.filter(project=self):
            skills.append(ps.skill)
        return skills

class ProjectSkill(models.Model):
    project = models.ForeignKey('Project')
    skill = models.ForeignKey('Skill')

    def __str__(self):
        return self.skill.name + ': ' + self.project.name

class ProjectImage(Entry):
    project = models.ForeignKey('Project')


