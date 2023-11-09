from django.db import models
from django.utils.translation import gettext as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Время создания'))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_('Время изменения'))

    class Meta:
        abstract = True
