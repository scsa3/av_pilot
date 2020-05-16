from collection.views import MovieList, MovieDetail
from django.urls import path

app_name = 'collection'
urlpatterns = [
    path('movies', MovieList.as_view(), name='movie-list'),
    path('movies/<int:pk>', MovieDetail.as_view(), name='movie-detail'),
]
