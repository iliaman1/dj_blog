from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy


class IsAuthorPermission:
    """
    Пользователи могут редактировать свои посты, но только для чтения для постов других авторов.
    """

    def has_permission(self):
        # Разрешения на чтение всегда допускаются, поэтому мы разрешаем GET, HEAD или OPTIONS.
        return self.get_object().author == self.request.user

    def dispatch(self, request, *args, **kwargs):
        # Разрешения на запись только для авторов постов.
        if not self.has_permission():
            return redirect('home')

        return super().dispatch(request, *args, **kwargs)
