from django.views import generic

from collection.models import Movie, Category


class MovieList(generic.ListView):
    model = Movie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context


class MovieDetail(generic.DetailView):
    model = Movie
