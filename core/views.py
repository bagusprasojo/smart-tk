from django.contrib.auth import get_user_model
from django.utils import timezone
from django.views.generic import TemplateView

from articles.models import Article
from mutabaah.models import Mutabaah
from students.models import Student
from .mixins import RoleRequiredMixin


class LandingPageView(TemplateView):
    template_name = 'core/landing.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(
            status=Article.Status.PUBLISHED
        )[:3]
        context['features'] = [
            'Landing page profesional',
            'Manajemen siswa & guru',
            'Mutabaah harian digital',
            'Download laporan PDF',
            'Role-based access control',
        ]
        return context


class DashboardView(RoleRequiredMixin, TemplateView):
    template_name = 'core/dashboard.html'
    allowed_roles = ['ADMIN', 'GURU', 'PARENT']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['student_count'] = Student.objects.count()
        context['mutabaah_count'] = Mutabaah.objects.count()
        context['article_count'] = Article.objects.count()
        entries = Mutabaah.objects.select_related('student', 'teacher')
        if user.role == 'GURU':
            entries = entries.filter(teacher=user)
        elif user.role == 'PARENT':
            entries = entries.filter(student__guardian=user)
        context['latest_entries'] = entries[:5]
        context['now'] = timezone.now()
        context['users_total'] = get_user_model().objects.count()
        return context
