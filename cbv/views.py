from django.shortcuts import render,HttpResponse
from django.views import View
from django.views.generic import TemplateView,ListView
from . import models
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
    