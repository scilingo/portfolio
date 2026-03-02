from django.views.generic import ListView, DetailView
from .models import Project

class ProjectListView(ListView):
    model = Project
    queryset = Project.objects.filter(is_active=True)
    template_name = 'projects/list.html'
    context_object_name = 'projects'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/detail.html'
    slug_field = 'slug'