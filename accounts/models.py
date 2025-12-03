from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom user model with explicit role choices."""

    class Roles(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        GURU = 'GURU', 'Guru'
        PARENT = 'PARENT', 'Orang Tua'

    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.ADMIN,
    )

    def is_admin(self):
        return self.role == self.Roles.ADMIN or self.is_superuser

    def is_guru(self):
        return self.role == self.Roles.GURU

    def is_parent(self):
        return self.role == self.Roles.PARENT
