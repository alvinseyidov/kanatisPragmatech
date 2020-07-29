from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView

from .forms import ContactForm
from .models import *


# Create your views here.
def common():
    context = {}
    context['text'] = TextPages.objects.order_by('-id').last()
    context["about"] = AboutUs.objects.order_by('-id').last()
    context['contact'] = Contact.objects.order_by('-id').last()
    context['allservices'] = Service.objects.order_by('-id').all()

    return context


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["carousels"] = Carousel.objects.all()[:15]
        context["services"] = Service.objects.order_by('-id')[:3]
        context["posts"] = Post.objects.order_by('-id')[:3]
        context["teams"] = Team.objects.order_by('-id')[:4]
        context["about"] = AboutUs.objects.order_by('-id').last()
        context['contact'] = Contact.objects.order_by('-id').last()
        context['allservices'] = Service.objects.order_by('-id').all()
        return context


class BlogPageView(ListView):
    model = Post
    paginate_by = 6
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contact.objects.order_by('-id').last()
        context["about"] = AboutUs.objects.order_by('-id').last()
        context['allservices'] = Service.objects.order_by('-id').all()
        return context
    


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contact.objects.order_by('-id').last()
        context["about"] = AboutUs.objects.order_by('-id').last()
        context['allservices'] = Service.objects.order_by('-id').all()
        return context


class ServicePageView(ListView):
    model = Service
    paginate_by = 2
    template_name = 'services.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.all()[:100]
        context['contact'] = Contact.objects.order_by('-id').last()
        context["about"] = AboutUs.objects.order_by('-id').last()
        return context


class SubServicePageView(ListView):
    template_name = 'services-type.html'
    model = SubService

    def get_context_data(self, **kwargs):
        context = super(SubServicePageView, self).get_context_data(**kwargs)
        context.update({
            'all': SubService.objects.all(),
            'page_title': 'Latest'
        })
        context['contact'] = Contact.objects.order_by('-id').last()
        context["about"] = AboutUs.objects.order_by('-id').last()
        return context


class SubServiceDetailView(TemplateView):
    template_name = 'services-type-detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(SubServiceDetailView, self).get_context_data(**kwargs)
 
        context['contact'] = Contact.objects.order_by('-id').last()
        context["about"] = AboutUs.objects.order_by('-id').last()
        return context


def aboutus(request):
    context = common()
    context['about'] = AboutUs.objects.order_by('-id').last()
    return render(request, 'about-us.html', context)


def teams(request):
    context = common()
    context['member'] = Team.objects.all().order_by('-id')
    return render(request, 'team.html', context)


def detail_team(request, slug):
    context = common()
    team = Team.objects.filter(slug=slug).order_by('-id').last()
    context['team'] = team
    context['services'] = TeamServices.objects.filter(service=team).order_by('-id').all()
    context['sertificate'] = SertificateTeam.objects.filter(sertificate=team).order_by('-id').all()
    return render(request, 'team-single-page.html', context)


def contactus(request):
    context = common()
    
    form = ContactForm()
    context['form'] = form
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kanatis:contact')

    return render(request, 'contact.html', context)
