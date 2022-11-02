from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.db.models import Q 
from university.models import University

# Create your views here.



class CreateView(CreateView):
    model = University
    fields = '__all__'
    success_url = reverse_lazy('university:list')

class ListUniversity(ListView):
    model = University
    paginate_by = 3

class DetailUniversity(DetailView):
    model = University

class SearchResultsView(ListView):
    model = University
    template_name = 'university\search_result.html'

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = University.objects.filter(
            Q(name__icontains=query) | Q(city__icontains=query)
        )
        return object_list