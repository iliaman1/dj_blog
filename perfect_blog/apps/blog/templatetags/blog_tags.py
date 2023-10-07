from django import template
from apps.blog.models import Category

register = template.Library()


@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    return Category.objects.filter(pk=filter)


@register.inclusion_tag('blog/list_categories.html')
def show_categories(cat_selected):
    return {'categories': Category.objects.all(), 'cat_selected': cat_selected}
