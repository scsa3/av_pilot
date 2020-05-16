from copy import deepcopy

from django.core.handlers.wsgi import WSGIRequest
from django.db.models import QuerySet
from django.views import generic

from collection.models import Movie, Category


class FilterList(generic.ListView):
    model = Movie

    def __init__(self, **kwargs):
        self.category_ids = set()
        super().__init__(**kwargs)

    def get(self, request: WSGIRequest, *args, **kwargs):
        self.set_category_ids(request)
        self.set_queryset()
        return super().get(request, *args, **kwargs)

    def set_category_ids(self, request: WSGIRequest):
        category_ids: list = request.GET.getlist('category')
        self.category_ids = set(category_ids)

    def set_queryset(self):
        movies = Movie.objects.all()
        for a_category in self.category_ids:
            movies = movies.filter(category=a_category)
        self.queryset = movies

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = self.get_movies_categories()
        return context

    def get_movies_categories(self):
        movie_ids = self.queryset.values_list('id', flat=True)
        categories = Category.objects.filter(movies__in=movie_ids)
        categories = queryset_to_dict(categories)
        return self.clean_categories(categories)

    @staticmethod
    def clean_categories(categories) -> dict:
        result = dict()
        for a_categories in categories:
            detail = result.setdefault(a_categories, {})
            detail["count"] = detail.setdefault("count", 0) + 1
        return result

    @staticmethod
    def add_url(categories: dict, querystring_category: list):
        # TODO: using this method in somewhere
        k: Category
        v: dict
        for k, v in categories.items():
            c_id = k.id
            link_ids = deepcopy(querystring_category)
            if c_id in link_ids:
                link_ids.remove(c_id)
            else:
                link_ids.append(c_id)
            v["querystring"] = "?categorys=" + "&categorys=".join(link_ids)


def add_or_remove(ids: set, check_id: str) -> set:
    result = deepcopy(ids)
    if check_id in ids:
        result.remove(check_id)
    else:
        result.add(check_id)
    return result


def queryset_to_dict(queryset: QuerySet) -> dict:
    result = dict()
    for a_query in queryset:
        result[a_query] = dict()
    return result


class Categories:
    def __init__(self, categories: QuerySet):
        self.origin = categories
        self.value = dict()

    def set_value(self):
        self.value = queryset_to_dict(self.origin)

    def set_count(self):
        for a_categories in self.origin:
            detail = self.value[a_categories]
            detail["count"] = detail.get("count", 0) + 1
