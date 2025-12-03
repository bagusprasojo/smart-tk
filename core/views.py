from django.contrib.auth import get_user_model
from django.utils import timezone
from django.views.generic import TemplateView

from articles.models import Article
from mutabaah.models import Mutabaah
from students.models import Student
from .mixins import RoleRequiredMixin


SCHOOL_PROFILE = {
    'name': 'TK Smart Cahaya',
    'tagline': 'Membangun karakter islami dan kemandirian sejak dini.',
    'description': (
        'TK Smart Cahaya adalah lembaga pendidikan anak usia dini yang fokus pada pembelajaran '
        'tematik, pembiasaan ibadah, dan keterampilan motorik melalui kegiatan kreatif. '
        'Sekolah kami berlokasi di Yogyakarta dengan lingkungan belajar yang aman dan penuh kasih sayang.'
    ),
    'vision': 'Mencetak generasi yang berakhlak mulia, cerdas, dan percaya diri.',
    'mission': [
        'Mengintegrasikan nilai-nilai islami pada setiap aktivitas belajar.',
        'Menyediakan program mutabaah harian untuk memantau perkembangan ibadah anak.',
        'Mendorong kreativitas, motorik, serta kemandirian melalui permainan edukatif.',
    ],
    'address': 'Jl. Mawar No. 10, Sleman, Yogyakarta',
    'operational_hours': 'Senin s/d Jumat, 07.30 - 12.00 WIB',
}

CONTACT_INFO = {
    'whatsapp_display': '+62 812-3456-7890',
    'whatsapp_link': '6281234567890',
    'email': 'info@tksmartcahaya.sch.id',
}


class LandingPageView(TemplateView):
    template_name = 'core/landing.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(
            status=Article.Status.PUBLISHED
        )[:3]
        context['features'] = [
            'Program hafalan ringan dengan mutabaah digital',
            'Kelas tematik dengan permainan kreatif',
            'Pelaporan perkembangan anak secara daring',
            'Kegiatan parenting bersama orang tua',
            'Manajemen konten sekolah terpadu',
        ]
        context['school_profile'] = SCHOOL_PROFILE
        context['contact_info'] = CONTACT_INFO
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
