from django.template.response import TemplateResponse
from django.views import generic
from extra_views import ModelFormSetView

from .models import Movie


class MovieFormSetView(ModelFormSetView):
    model = Movie
    fields = '__all__'
    template_name = 'movie_formset.html'

    def get(self, request, *args, **kwargs):
        response: TemplateResponse = super().get(request, *args, **kwargs)
        print(response.context_data)
        return response


class MovieList(generic.ListView):
    model = Movie


class MovieDetail(generic.DetailView):
    model = Movie
