from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import (
    Carousel, Service, Post
)


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["carousels"] = Carousel.objects.all()[:15]
        context["services"] = Service.objects.order_by('-id')[:3]
        return context


class BlogPageView(ListView):
    model = Post
    paginate_by = 6
    template_name = 'blog.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ServicePageView(ListView):
    model = Service
    paginate_by = 2
    template_name = 'services.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["services"] = Service.objects.all()[:100]
        
        return context

