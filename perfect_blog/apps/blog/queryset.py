from django.db import models
from django.db.models import F
from django.db.models import Count


class PostQuerySet(models.QuerySet):
    def is_published(self):
        return self.filter(is_published=True)

    def annotate_rating(self):
        return self.annotate(
            number_of_likes=Count("likes"),
            number_of_dislikes=Count("dislikes"),
            rating=F('number_of_likes') - F('number_of_dislikes')
        )

    def is_author(self, user):
        return self.filter(author=user.pk)
