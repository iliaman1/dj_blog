from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=64, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Post(models.Model):
    title = models.CharField(max_length=128, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Текст поста')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категории')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['time_create', 'title']
