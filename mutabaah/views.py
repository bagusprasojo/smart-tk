from django.http import HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from core.mixins import RoleRequiredMixin
from .forms import MutabaahForm
from .models import Mutabaah


class MutabaahListView(RoleRequiredMixin, ListView):
    template_name = 'mutabaah/mutabaah_list.html'
    context_object_name = 'entries'
    model = Mutabaah
    allowed_roles = ['ADMIN', 'GURU', 'PARENT']

    def get_queryset(self):
        qs = super().get_queryset().select_related('student', 'teacher')
        user = self.request.user
        if user.role == 'GURU':
            qs = qs.filter(teacher=user)
        elif user.role == 'PARENT':
            qs = qs.filter(student__guardian=user)
        student_id = self.request.GET.get('student')
        if student_id:
            qs = qs.filter(student_id=student_id)
        return qs


class MutabaahCreateView(RoleRequiredMixin, CreateView):
    template_name = 'mutabaah/mutabaah_form.html'
    form_class = MutabaahForm
    success_url = reverse_lazy('mutabaah_list')
    allowed_roles = ['ADMIN', 'GURU']

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.teacher = self.request.user
        return super().form_valid(form)


class MutabaahUpdateView(RoleRequiredMixin, UpdateView):
    template_name = 'mutabaah/mutabaah_form.html'
    form_class = MutabaahForm
    success_url = reverse_lazy('mutabaah_list')
    allowed_roles = ['ADMIN', 'GURU']
    model = Mutabaah

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.role == 'GURU':
            qs = qs.filter(teacher=self.request.user)
        return qs


class MutabaahDetailView(RoleRequiredMixin, DetailView):
    template_name = 'mutabaah/mutabaah_detail.html'
    context_object_name = 'entry'
    allowed_roles = ['ADMIN', 'GURU', 'PARENT']
    model = Mutabaah

    def has_role_permission(self):
        entry = self.get_object()
        user = self.request.user
        if user.role == 'PARENT':
            return entry.student.guardian == user
        if user.role == 'GURU':
            return entry.teacher == user
        return super().has_role_permission()


class MutabaahPDFView(MutabaahDetailView):
    """Render mutabaah entry into PDF using WeasyPrint."""

    def render_to_response(self, context, **response_kwargs):
        from weasyprint import HTML  # Lazy import to avoid fontconfig errors on load.
        html = render_to_string('mutabaah/mutabaah_pdf.html', context)
        pdf = HTML(
            string=html,
            base_url=self.request.build_absolute_uri(),
        ).write_pdf()
        response = HttpResponse(pdf, content_type='application/pdf')
        entry = context['entry']
        response['Content-Disposition'] = f'attachment; filename=mutabaah-{entry.student.name}-{entry.date}.pdf'
        return response
