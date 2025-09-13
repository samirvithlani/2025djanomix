from django.shortcuts import render,HttpResponse
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView
from . import models
from django.urls import reverse_lazy
# Create your views here.
#View
class MyView(View):
    def get(self,request):
        return HttpResponse("Hello this is class based view")
    
    # def post(self,request):
    #     return HttpResponse("Hello this is class based views..")

class HomePageView(TemplateView):
    template_name ="home.html"


class SportsListView(ListView):
    model = models.Sports
    template_name = "sports/sportsList.html"    
    context_object_name = "sports" 
    #paginate_by =2
    paginate_orphans=False
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "ALL SPORTS"
        context['totalSports'] = self.get_queryset().count()
        print(context)
        return context
    
    def get_ordering(self):
        order = self.request.GET.get("name","origin")
        return order
    

class SportsCreateView(CreateView):
    model = models.Sports
    template_name = "sports/sports_create.html"        
    fields = "__all__"
    success_url = reverse_lazy("sportslist")
    #skwarg{pk:"",slug:""}
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] ="this is sports creation page"
        return context
    
    def form_valid(self,form):
        #user loggedin --> sports create..
        print("form...",form)
        print("//",form.instance.origin)
        form.instance.name = form.instance.name.upper() 
        return super().form_valid(form)
    
    def get_success_url(self):
        #return super().get_success_url()
        return reverse_lazy("sportdetail",kwargs={'pk':self.object.pk})


class SportsDetailView(DetailView):
    model = models.Sports
    context_object_name="sports"
    template_name = "sports/sport_Detail.html"    
    
    def get_queryset(self):
        return super().get_queryset()
    
    
    