from turtle import home
from django.urls import path
from .views import  CreateView, ListUniversity, DetailUniversity, SearchResultsView
from django.views.decorators.cache import cache_page

app_name = 'university'

urlpatterns = [
    path('',ListUniversity.as_view(), name = 'list' ), 
    path('detail/<int:pk>', DetailUniversity.as_view(), name = 'detail' ),
    path('create/', CreateView.as_view(), name= 'create'),
    path('search/', cache_page(60 * 1)(SearchResultsView.as_view()), name = 'search') #cache for one minute


]