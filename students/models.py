from django.conf import settings
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=150)
    class_name = models.CharField(max_length=50)
    parents_name = models.CharField(max_length=150)
    parents_phone = models.CharField(max_length=30)
    guardian = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='children',
        blank=True,
        null=True,
        help_text='Opsional pengguna dengan role orang tua yang dapat memantau.',
    )
    photo = models.ImageField(upload_to='students/photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
