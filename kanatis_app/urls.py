from django.urls import path
from .views import HomePageView, aboutus, teams, detail_team,contactus

app_name = 'kanatis'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('about/', aboutus, name='about'),
    path('contact/', contactus, name='contact'),
    path('teams/', teams, name='teams'),
    path('team/<int:pk>/', detail_team, name='detail_team'),
]
