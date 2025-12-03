from django.contrib.auth import get_user_model, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from core.mixins import RoleRequiredMixin
from .forms import LoginForm, UserForm


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm


def logout_view(request):
    """Logout helper allowing GET requests and redirecting to landing page."""
    logout(request)
    return redirect('landing')


class UserListView(RoleRequiredMixin, ListView):
    template_name = 'accounts/user_list.html'
    context_object_name = 'users'
    allowed_roles = ['ADMIN']

    def get_queryset(self):
        User = get_user_model()
        return User.objects.order_by('username')


class UserCreateView(RoleRequiredMixin, CreateView):
    template_name = 'accounts/user_form.html'
    form_class = UserForm
    success_url = reverse_lazy('user_list')
    allowed_roles = ['ADMIN']
