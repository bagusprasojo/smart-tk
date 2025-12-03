from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied


class RoleRequiredMixin(LoginRequiredMixin):
    """Mixin that checks whether the current user has one of the allowed roles."""

    allowed_roles = None  # Iterable of role names from accounts.User.Roles

    def dispatch(self, request, *args, **kwargs):
        if not self.has_role_permission():
            raise PermissionDenied('Anda tidak memiliki akses ke halaman ini.')
        return super().dispatch(request, *args, **kwargs)

    def has_role_permission(self):
        if not self.allowed_roles:
            return True
        user = self.request.user
        if not user.is_authenticated:
            return False
        if user.is_superuser:
            return True
        return user.role in self.allowed_roles
