from datetime import timedelta

from django.db import models
from django.db.models import F, Q
from django.db.models import Count
from django.utils import timezone


class PostQuerySet(models.QuerySet):

    def is_author(self, user):
        return self.filter(author=user.pk)

    def is_published(self):
        return self.filter(is_published=True)

    def annotate_rating(self, period: Q = Q()):
        """
        Вычисляем рейтинг для постов за определенный период,
        по умолчанию для всего периода.
        """

        return self.annotate(
            upvotes=Count("votes", filter=Q(vote__positive=True) & period),
            downvotes=Count("votes", filter=Q(vote__positive=False) & period),
            rating=F("upvotes") - F("downvotes")
        )

    def best_of_period(self, period: timedelta):
        assert isinstance(period, timedelta), 'period should be timedelta instance'

        now = timezone.now()

        return (
            self.filter(
                created_at__gte=now - period
            )
            .annotate_rating(
                Q(vote__created_at__gte=now - period)
            )
            .order_by('-rating')
        )
