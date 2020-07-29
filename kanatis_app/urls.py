from django.urls import path
from .views import (
    HomePageView, ServicePageView, BlogPageView,
    BlogDetailView
)
app_name='kanatis'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('services/', ServicePageView.as_view(), name='services'),
    path('news/', BlogPageView.as_view(), name='blog'),
    path('news/<str:slug>', BlogDetailView.as_view(), name='blog_detail'),
]