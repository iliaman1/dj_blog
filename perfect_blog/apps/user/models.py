from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse

from core.models import BaseModel


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(unique=True, max_length=50, blank=True, null=True)
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='images/profile/%Y/%m/%d/',
        default='images/profile/default_ava.jpg'
    )
    bio = models.TextField(null=True, blank=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    following = models.ManyToManyField(
        'self',
        verbose_name='Подписки',
        related_name='followers',
        symmetrical=False,
        blank=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('showprofile', kwargs={'name': self.name})

    class Meta:
        ordering = ['created_at']
        verbose_name = _('Профиль')
        verbose_name_plural = _('Профили')
