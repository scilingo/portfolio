from django.db import models

class Certificate(models.Model):
    title       = models.CharField(max_length=300)
    issuer      = models.CharField(max_length=200)
    date        = models.DateField()
    image       = models.ImageField(upload_to='certificates/', blank=True)
    file        = models.FileField(upload_to='certificates/pdf/', blank=True)
    url         = models.URLField(blank=True)
    is_active   = models.BooleanField(default=True)
    order       = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-date']
        verbose_name = "Certificado"

class Publication(models.Model):
    title    = models.CharField(max_length=300)
    authors  = models.TextField()
    journal  = models.CharField(max_length=200, blank=True)
    year     = models.PositiveIntegerField()
    url      = models.URLField(blank=True)
    abstract = models.TextField(blank=True)

    class Meta:
        ordering = ['-year']
        verbose_name = "Publicação"