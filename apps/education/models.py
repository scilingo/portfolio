from django.db import models

class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree      = models.CharField(max_length=200)       # "Engenharia Biomédica"
    field       = models.CharField(max_length=200, blank=True)
    start_date  = models.DateField()
    end_date    = models.DateField(null=True, blank=True)
    in_progress = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    logo        = models.ImageField(upload_to='education/', blank=True)
    order       = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-start_date']
        verbose_name = "Formação"

class Experience(models.Model):
    TYPES = [('work','Trabalho'), ('research','Iniciação Científica'),
             ('volunteer','Voluntário'), ('extracurricular','Extracurricular')]

    organization = models.CharField(max_length=200)
    role         = models.CharField(max_length=200)
    type         = models.CharField(max_length=20, choices=TYPES)
    start_date   = models.DateField()
    end_date     = models.DateField(null=True, blank=True)
    current      = models.BooleanField(default=False)
    description  = models.TextField(blank=True)
    logo         = models.ImageField(upload_to='experience/', blank=True)
    order        = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-start_date']
        verbose_name = "Experiência"