from movies.views import MovieList, MovieDetail
from django.urls import path

app_name = 'category'
urlpatterns = [
    path('', MovieList.as_view(), name='list'),
    path('<int:pk>', MovieDetail.as_view(), name='detail'),
]
