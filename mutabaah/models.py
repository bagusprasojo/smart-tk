from django.conf import settings
from django.db import models

from students.models import Student


class Mutabaah(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='mutabaah')
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='mutabaah_entries',
    )
    date = models.DateField()
    ibadah = models.TextField()
    sikap = models.TextField()
    hafalan = models.TextField()
    motorik = models.TextField()
    kemandirian = models.TextField()
    catatan = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.student.name} - {self.date}'
