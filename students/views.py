from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView

from core.mixins import RoleRequiredMixin
from .forms import StudentForm
from .models import Student


class StudentListView(RoleRequiredMixin, ListView):
    template_name = 'students/student_list.html'
    context_object_name = 'students'
    allowed_roles = ['ADMIN', 'GURU']
    model = Student


class StudentCreateView(RoleRequiredMixin, CreateView):
    template_name = 'students/student_form.html'
    form_class = StudentForm
    success_url = reverse_lazy('student_list')
    allowed_roles = ['ADMIN']


class StudentDetailView(RoleRequiredMixin, DetailView):
    template_name = 'students/student_detail.html'
    context_object_name = 'student'
    allowed_roles = ['ADMIN', 'GURU', 'PARENT']
    model = Student

    def has_role_permission(self):
        user = self.request.user
        student = self.get_object()
        if user.role == 'PARENT':
            return student.guardian == user
        return super().has_role_permission()
