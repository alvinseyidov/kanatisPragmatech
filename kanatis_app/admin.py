from django.contrib import admin
from .models import *


admin.site.register(Post)
admin.site.register(Carousel)
admin.site.register(Service)
admin.site.register(SubService)
admin.site.register(Logo)

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
