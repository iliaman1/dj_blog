from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, blank=True, null=True)
    full_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Время создания'))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_('Время изменения'))

    class Meta:
        ordering = ['created_at']
        verbose_name = _('Профиль')
        verbose_name_plural = _('Профили')

    def __str__(self):
        return self.user.username
