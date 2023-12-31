from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

from core.models import BaseModel
from .queryset import PostQuerySet



class Category(models.Model):
    name = models.CharField(max_length=64, db_index=True, verbose_name=_('Категория'))
    slug = models.SlugField(max_length=128, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')
        ordering = ['id']


class Post(BaseModel):
    preview = models.ImageField(
        null=True,
        blank=True,
        upload_to='images/preview/%Y/%m/%d/',
        default='images/preview/default_preview.jpg',
        verbose_name='Превью'
    )
    title = models.CharField(max_length=128, verbose_name=_('Заголовок'))
    slug = models.SlugField(max_length=128, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name=_('Текст поста'))
    is_published = models.BooleanField(default=True, verbose_name=_('Публикация'))
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Автор'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Категории'))
    votes = models.ManyToManyField(User, related_name='votes_set', through='Vote', blank=True)

    objects = PostQuerySet.as_manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = _('Пост')
        verbose_name_plural = _('Посты')
        ordering = ['created_at', 'title']


class Vote(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    positive = models.BooleanField()


class Comment(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Комментарий')
        verbose_name_plural = _('Комментарии')

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.post.slug})
