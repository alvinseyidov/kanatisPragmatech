from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from .forms import ContactForm
from .models import *
from django.utils import translation


# Create your views here.
def common():
    context = {}
    context['text'] = TextPages.objects.order_by('-id').last()
    context['contact'] = Contact.objects.order_by('-id').last()
    return context


def set_language(request, lang_code):
    lang = request.META.get("HTTP_REFERER", None)
    if not lang:
        lang = "/"
    if "az" in lang:
        lang = lang.replace("az", lang_code)
    elif "en" in lang:
        lang = lang.replace("en", lang_code)

    response = redirect(lang)
    request.session[translation.LANGUAGE_SESSION_KEY] = lang_code

    return response


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["carousels"] = Carousel.objects.all()[:15]
        context["services"] = Service.objects.order_by('-id')[:4]
        context["posts"] = Post.objects.order_by('-id')[:3]
        context['contact'] = Contact.objects.order_by('-id').last()
        return context


class BlogPageView(ListView):
    model = Post
    paginate_by = 6
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contact.objects.order_by('-id').last()
        context['recentposts'] = Post.objects.order_by('-id')[:8]
        return context


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contact.objects.order_by('-id').last()
        return context


class ServicePageView(ListView):
    model = Service
    template_name = 'services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.all()[:100]
        context['contact'] = Contact.objects.order_by('-id').last()
        return context


class SubServicePageView(TemplateView):
    template_name = 'services-type.html'
    model = SubService

    def get_context_data(self, **kwargs):
        context = super(SubServicePageView, self).get_context_data(**kwargs)
        service = kwargs.get('service')
        if service:
            context['servicetypes'] = SubService.objects.order_by('-id').filter(service__slug=service)
        context['contact'] = Contact.objects.order_by('-id').last()
        return context


class SubServiceDetailView(TemplateView):
    template_name = 'services-type-detail.html'
    model = SubService

    def get_context_data(self, **kwargs):
        context = super(SubServiceDetailView, self).get_context_data(**kwargs)
        subservice = kwargs.get('subservice')
        service = kwargs.get('service')
        if subservice:
            context['subservice'] = SubService.objects.order_by('-id').filter(slug=subservice).first()
        if service:
            context['subservices'] = SubService.objects.order_by('-id').filter(service__slug=service)
        context['contact'] = Contact.objects.order_by('-id').last()
        return context


class SubAboutDetailView(TemplateView):
    template_name = 'subabout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subabout'] = SubAboutUs.objects.filter(slug = context['slug']).first()
        context['contact'] = Contact.objects.order_by('-id').last()
        return context
    


def aboutus(request):
    context = common()
    return render(request, 'about-us.html', context)


def teams(request):
    context = common()
    context['member'] = Team.objects.all().order_by('order')
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
