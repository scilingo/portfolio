from django.db import models

class SkillCategory(models.Model):
    name  = models.CharField(max_length=100)   # "Programação", "Idiomas", etc.
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

class Skill(models.Model):
    LEVELS = [(1,'Básico'),(2,'Intermediário'),(3,'Avançado'),(4,'Especialista')]

    name     = models.CharField(max_length=100)
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE,
                                  related_name='skills')
    level    = models.IntegerField(choices=LEVELS, default=2)
    icon     = models.CharField(max_length=10, blank=True)   # emoji ou class CSS
    order    = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']