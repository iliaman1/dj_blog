from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=64, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=128, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'  # tyt
        ordering = ['id']


class Post(models.Model):
    title = models.CharField(max_length=128, verbose_name='Заголовок')
    slug = models.SlugField(max_length=128, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Текст поста')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категории')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['created_at', 'title']


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.post.slug})
