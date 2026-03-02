from django.db import models

class Profile(models.Model):
    name            = models.CharField(max_length=100)
    title           = models.CharField(max_length=200)          # "Engenheira Biomédica"
    bio             = models.TextField()
    photo_hero      = models.ImageField(upload_to='profile/')   # Foto sem fundo
    photo_about     = models.ImageField(upload_to='profile/')   # Foto no lab
    linkedin_url    = models.URLField(blank=True)
    instagram_url   = models.URLField(blank=True)
    email           = models.EmailField(blank=True)
    phone           = models.CharField(max_length=20, blank=True)
    is_active       = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Perfil"

    def __str__(self): return self.name