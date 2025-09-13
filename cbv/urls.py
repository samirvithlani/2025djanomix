from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("myfun/",views.MyView.as_view(),name="myfun"),
    path("home/",views.HomePageView.as_view()),
    path("sportslist/",views.SportsListView.as_view(),name='sportslist'),
    path("createsport/",views.SportsCreateView.as_view(),name="createsport"),
    path("sportsdetail/<int:pk>",views.SportsDetailView.as_view(),name="sportdetail")
]