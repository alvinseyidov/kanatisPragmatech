from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(AboutUs)
admin.site.register(Contact)
admin.site.register(ContactUs)

admin.site.register(TextPages)


class Service(admin.StackedInline):
    model = TeamServices
    extra = 5


class Sertificate(admin.StackedInline):
    model = SertificateTeam
    extra = 5


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    inlines = [Service, Sertificate]
    list_display = ['name', 'desc']
