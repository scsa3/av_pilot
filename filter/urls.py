from filter.views import FilterList
from django.urls import path

app_name = 'filter'
urlpatterns = [
    path('', FilterList.as_view(), name='filter-list'),
]
