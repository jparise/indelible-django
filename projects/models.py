from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=160)
    slug = models.SlugField(unique=True)
    desc = models.TextField()
    link = models.URLField()

    class Meta:
        verbose_name_plural = 'Projects'

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return self.link
