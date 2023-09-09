from .models import Category

nav_menu = [
    {'title': 'Создать пост', 'url_name': 'addpost'},
    {'title': 'О всяком', 'url_name': 'about'},
    {'title': 'Войти', 'url_name': 'login'}
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        categories = Category.objects.all()
        user_nav_menu = nav_menu.copy()
        if not self.request.user.is_authenticated:
            del user_nav_menu[0]
        context['nav_menu'] = user_nav_menu
        context['categories'] = categories
        if 'cat_selected' not in context:
            context['cat_selected'] = 0

        return context
