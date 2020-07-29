from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView

from .forms import ContactForm
from .models import *


# Create your views here.
def common():
    context = {}
    context['text'] = TextPages.objects.last()
    return context


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


def aboutus(request):
    context = common()
    context['about'] = AboutUs.objects.last()
    return render(request, 'about-us.html', context)


def teams(request):
    context = common()
    context['member'] = Team.objects.all()
    return render(request, 'team.html', context)


def detail_team(request, pk):
    context = common()
    team = Team.objects.filter(pk=pk).last()
    context['team'] = team
    context['services'] = TeamServices.objects.filter(service=team).all()
    context['sertificate'] = SertificateTeam.objects.filter(sertificate=team).all()
    return render(request, 'team-single-page.html', context)


def contactus(request):
    context = common()
    context['contact'] = Contact.objects.last()
    form = ContactForm()
    context['form'] = form
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kanatis:contact')

    return render(request, 'contact.html', context)
