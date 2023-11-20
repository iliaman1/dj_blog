nav_menu = [
    {'title': 'Создать пост', 'url_name': 'addpost'},
    {'title': 'Мои посты', 'url_name': 'myposts'},
    {'title': 'О всяком', 'url_name': 'about'}
]


class BaseDataMixin:
    additional_context = {}

    def get_context_data(self, **kwargs):
        context = kwargs | self.additional_context
        user_nav_menu = nav_menu.copy()
        if not self.request.user.is_authenticated:
            del user_nav_menu[0]
            del user_nav_menu[0]
        context['nav_menu'] = user_nav_menu
        return super().get_context_data(**context)
