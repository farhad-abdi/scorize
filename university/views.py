from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.db.models import Q 
from university.models import University
#from django.utils.functional import cached_property 
from django.views.decorators.cache import cache_page


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

#@cache_page(60 * 1) #cache for one minute
class SearchResultsView(ListView):
    model = University
    template_name = 'university\search_result.html'

    #@cached_property
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = University.objects.filter(
            Q(name__icontains=query) | Q(city__icontains=query)
        )
        return object_list