from core.utils import BaseDataMixin
from .models import Category


class DataMixin(BaseDataMixin):
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()

        if 'cat_selected' not in context:
            context['cat_selected'] = 0

        return context
