from django.contrib import admin
from .models import *

# admin.site.register(Post)
# admin.site.register(Carousel)
admin.site.register(Service)
admin.site.register(SubService)
admin.site.register(Logo)

# Register your models here.
# admin.site.register(AboutUs)
# admin.site.register(Contact)
admin.site.register(ContactUs)


# admin.site.register(TextPages)


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


# class ServiceAdmin(admin.ModelAdmin):
#     fields = [
#         'name_az', 'name_en', 'name_ru',
#         'description_az', 'description_en', 'description_ru',
#         'image', 'fa_class', 'slug'
#
#     ]
#
#
# admin.site.register(Service, ServiceAdmin)
#
#
# class SubServiceAdmin(admin.ModelAdmin):
#     fields = [
#         'title_az', 'title_en', 'title_ru',
#         'description_az', 'description_en', 'description_ru',
#         'image', 'fa_icon', 'service', 'slug',
#
#     ]
#
#
# admin.site.register(SubService, SubServiceAdmin)

#
# class SubServiceAdmin(admin.ModelAdmin):
#     fields = [
#         'team_member_az', 'team_member_en', 'team_member_ru',
#         'team_az', 'team_en', 'team_ru',
#         'image', 'fa_icon', 'service', 'slug',
#
#     ]
#
#
# admin.site.register(SubService, SubServiceAdmin)


class AboutAdmin(admin.ModelAdmin):
    fields = [
        'title_az', 'title_en', 'title_ru',
        'description_az', 'description_en', 'description_ru',
        'img'

    ]


admin.site.register(AboutUs, AboutAdmin)


class ContactAdmin(admin.ModelAdmin):
    fields = [
        'address_az', 'address_en', 'address_ru',
        'gmap_embed_address_az', 'gmap_embed_address_en', 'gmap_embed_address_ru',
        'text_az', 'text_en', 'text_ru',
        'gmap_embed_address', 'office_hour', 'number',

    ]


admin.site.register(Contact, ContactAdmin)
