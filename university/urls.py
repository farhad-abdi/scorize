from turtle import home
from django.urls import path
from .views import  CreateView, ListUniversity, DetailUniversity, SearchResultsView

app_name = 'university'

urlpatterns = [
    path('',ListUniversity.as_view(), name = 'list' ), 
    path('detail/<int:pk>', DetailUniversity.as_view(), name = 'detail' ),
    path('create/', CreateView.as_view(), name= 'create'),
    path('search/', SearchResultsView.as_view(), name = 'search')


]