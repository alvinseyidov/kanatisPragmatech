from django.contrib import admin
from .models import *

admin.site.register(ContactUs)


@admin.register(SertificateTeam)
class SertificateTeamAdmin(admin.ModelAdmin):
    ...


@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if self.model.objects.count() >= 5:
            return False
        return super().has_add_permission(request)


class PostAdmin(admin.ModelAdmin):
    fields = [
        'title_az', 'title_en',
        'short_content_az', 'short_content_en',
        'content_az', 'content_en',
        'image', 'category'

    ]


admin.site.register(Post, PostAdmin)


class TextPagesAdmin(admin.ModelAdmin):
    fields = [
        'team_member_az', 'team_member_en',
        'team_az', 'team_en',

    ]


admin.site.register(TextPages, TextPagesAdmin)


class CarouselAdmin(admin.ModelAdmin):
    fields = [
        'content_az', 'content_en',
        'image', 'service'

    ]


admin.site.register(Carousel, CarouselAdmin)


class ServiceAdmin(admin.ModelAdmin):
    fields = [
        'name_az', 'name_en',
        'description_az', 'description_en',
        'order', 'image'

    ]


admin.site.register(Service, ServiceAdmin)


class SubServiceAdmin(admin.ModelAdmin):
    fields = [
        'title_az', 'title_en', 'order',
        'content_az', 'content_en',
        'image', 'service',

    ]


admin.site.register(SubService, SubServiceAdmin)


class TeamAdmin(admin.ModelAdmin):
    fields = [
        'name_az', 'name_en',
        'short_desc_az', 'short_desc_en',
        'desc_az', 'desc_en',
        'status_az', 'status_en',
        'order', 'email', 'number',
        'img', 'facebook', 'instagram',
        'twitter'

    ]


admin.site.register(Team, TeamAdmin)


class AboutAdmin(admin.ModelAdmin):
    fields = [
        'title_az', 'title_en',
        'description_az', 'description_en',
        'img'

    ]

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


admin.site.register(AboutUs, AboutAdmin)


class SubAboutAdmin(admin.ModelAdmin):
    fields = [
        'title_az', 'title_en',
        'description_az', 'description_en',
        'order',
        'img', 'about'

    ]

    def has_add_permission(self, request):
        if self.model.objects.count() >= 10:
            return False
        return super().has_add_permission(request)


admin.site.register(SubAboutUs, SubAboutAdmin)


class ContactAdmin(admin.ModelAdmin):
    fields = [
        'address_az', 'address_en',
        'text_az', 'text_en',
        'gmap_embed_address', 'office_hour',
        'number', 'office_phone', 'social_networks'

    ]

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


admin.site.register(Contact, ContactAdmin)


# class ContactUsAdmin(admin.ModelAdmin):
#     fields = [
#         'address_az', 'address_en',
#         'text_az', 'text_en',
#         'gmap_embed_address', 'office_hour',
#         'number', 'office_phone', 'social_networks'
#
#     ]
#
#     def has_add_permission(self, request):
#         if self.model.objects.count() >= 1:
#             return False
#         return super().has_add_permission(request)
#
#
# admin.site.register(Contact, ContactAdmin)
