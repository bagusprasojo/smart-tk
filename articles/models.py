from django.conf import settings
from django.db import models
from django.urls import reverse


class Article(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DRAFT', 'Draft'
        PUBLISHED = 'PUBLISHED', 'Published'

    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='articles',
    )
    hero_image = models.ImageField(upload_to='articles/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[self.pk])
