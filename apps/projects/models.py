from django.db import models

class ProjectTag(models.Model):
    name  = models.CharField(max_length=50)
    color = models.CharField(max_length=7, default='#2d7a4f')  # hex

    def __str__(self): return self.name

class Project(models.Model):
    title       = models.CharField(max_length=200)
    slug        = models.SlugField(unique=True)
    description = models.TextField()
    image       = models.ImageField(upload_to='projects/', blank=True)
    tags        = models.ManyToManyField(ProjectTag, blank=True)
    repo_url    = models.URLField(blank=True)
    demo_url    = models.URLField(blank=True)
    date        = models.DateField()
    order       = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    is_active   = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', '-date']
        verbose_name = "Projeto"

    def __str__(self): return self.title