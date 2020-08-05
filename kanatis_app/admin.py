from django.contrib import admin
from .models import *

admin.site.register(Logo)

admin.site.register(ContactUs)


# class Service(admin.StackedInline):
#     model = TeamServices
#     extra = 5
#     fields =[
#         'name_az', 'name_en'
#     ]

# class Sertificate(admin.StackedInline):
#     model = SertificateTeam
#     extra = 5


# @admin.register(Team)
# class TeamAdmin(admin.ModelAdmin):
#     inlines = [Service, Sertificate]
#     list_display = ['name', 'desc']

@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if self.model.objects.count() >= 5:
            return False
        return super().has_add_permission(request)


class PostAdmin(admin.ModelAdmin):
    fields = [
        'title_az', 'title_en', 'title_ru',
        'content_az', 'content_en', 'content_ru',
        'image', 'category'

    ]


admin.site.register(Post, PostAdmin)


class TextPagesAdmin(admin.ModelAdmin):
    fields = [
        'team_member_az', 'team_member_en', 'team_member_ru',
        'team_az', 'team_en', 'team_ru',

    ]


admin.site.register(TextPages, TextPagesAdmin)


class CarouselAdmin(admin.ModelAdmin):
    fields = [
        'content_az', 'content_en', 'content_ru',
        'image', 'service'

    ]


admin.site.register(Carousel, CarouselAdmin)


class ServiceAdmin(admin.ModelAdmin):
    fields = [
        'name_az', 'name_en', 'name_ru',
        'description_az', 'description_en', 'description_ru',
        'image', 'fa_class'

    ]


admin.site.register(Service, ServiceAdmin)


class SubServiceAdmin(admin.ModelAdmin):
    ...
    # fields = [
    #     'title_az', 'title_en', 'title_ru',
    #     'description_az', 'description_en', 'description_ru',
    #     'image', 'fa_icon', 'service',

    # ]


admin.site.register(SubService, SubServiceAdmin)


class TeamAdmin(admin.ModelAdmin):
    pass


admin.site.register(Team, TeamAdmin)


class AboutAdmin(admin.ModelAdmin):
    fields = [
        'title_az', 'title_en', 'title_ru',
        'description_az', 'description_en', 'description_ru',
        'img'

    ]
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


admin.site.register(AboutUs, AboutAdmin)


class ContactAdmin(admin.ModelAdmin):
    fields = [
        'address_az', 'address_en', 'address_ru',
        'text_az', 'text_en', 'text_ru',
        'gmap_embed_address', 'office_hour', 'number','social_networks'

    ]

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

admin.site.register(Contact, ContactAdmin)
