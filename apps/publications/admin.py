from django.contrib import admin
from .models import Certificate, Publication

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display  = ['title', 'issuer', 'date', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    search_fields = ['title', 'issuer']

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display  = ['title', 'year']
    search_fields = ['title', 'authors']