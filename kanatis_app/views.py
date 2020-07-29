from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import ContactForm
from .models import *


# Create your views here.
def common():
    context = {}
    context['text'] = TextPages.objects.last()
    return context


class HomePageView(TemplateView):
    template_name = 'index.html'


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
