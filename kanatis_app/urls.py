from django.urls import path
from .views import (
    HomePageView, ServicePageView, BlogPageView,
    BlogDetailView, aboutus, teams, detail_team,contactus, SubServicePageView,
    SubServiceDetailView
)
app_name='kanatis'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('services/', ServicePageView.as_view(), name='services'),
    path('services/<str:service>/', SubServicePageView.as_view(), name='services-type'),
    path('services/<str:service>/<str:subservice>/', SubServiceDetailView.as_view(), name='service-detail'),
    path('news/', BlogPageView.as_view(), name='blog'),
    path('news/<str:slug>', BlogDetailView.as_view(), name='blog_detail'),
    path('about/', aboutus, name='about'),
    path('contact/', contactus, name='contact'),
    path('teams/', teams, name='teams'),
    path('teams/<str:slug>/', detail_team, name='detail_team'),
]
