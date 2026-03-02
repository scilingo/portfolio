from django.views.generic import TemplateView
from apps.about.models import Profile
from apps.projects.models import Project
from apps.education.models import Education, Experience
from apps.skills.models import SkillCategory
from apps.publications.models import Certificate

class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['profile']      = Profile.objects.filter(is_active=True).first()
        ctx['projects']     = Project.objects.filter(is_active=True)
        ctx['educations']   = Education.objects.all()
        ctx['experiences']  = Experience.objects.all()
        ctx['skill_cats']   = SkillCategory.objects.prefetch_related('skills').all()
        ctx['certificates'] = Certificate.objects.filter(is_active=True)
        return ctx
