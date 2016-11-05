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


class Project(Entry):
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # display null as ongoing
    # https://github.com/niwinz/djorm-pgarray
    # http://dba.stackexchange.com/questions/60132/foreign-key-constraint-on-array-member
    # skill_ids = djorm_pgarray.fields.IntegerArrayField(default=[])
    skill = models.ForeignKey('Skill', null=True, blank=True)
    is_demo = models.BooleanField(default=False)


class ProjectImage(Entry):
    project = models.ForeignKey('Project')