from modeltranslation.translator import translator, TranslationOptions
from .models import *


class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'short_content', 'content')


translator.register(Post, PostTranslationOptions)


class CarouselTranslationOptions(TranslationOptions):
    fields = ('content',)


translator.register(Carousel, CarouselTranslationOptions)


class ServiceTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


translator.register(Service, ServiceTranslationOptions)


class SubServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


translator.register(SubService, SubServiceTranslationOptions)


class TextPagesTranslationOptions(TranslationOptions):
    fields = ('team_member', 'team',)


translator.register(TextPages, TextPagesTranslationOptions)


class AboutUsTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


translator.register(AboutUs, AboutUsTranslationOptions)


class SubAboutUsTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


translator.register(SubAboutUs, SubAboutUsTranslationOptions)


class TeamTranslationOptions(TranslationOptions):
    fields = ('name', 'short_desc', 'desc', 'status')


translator.register(Team, TeamTranslationOptions)


class TeamServicesTranslationOptions(TranslationOptions):
    fields = ('serv_name',)


translator.register(TeamServices, TeamServicesTranslationOptions)


class SertificateTeamTranslationOptions(TranslationOptions):
    fields = ('sertificate_name',)


translator.register(SertificateTeam, SertificateTeamTranslationOptions)


class ContactTranslationOptions(TranslationOptions):
    fields = ('address', 'gmap_embed_address', 'text')


translator.register(Contact, ContactTranslationOptions)


class ContactFormTranslationOptions(TranslationOptions):
    fields = ('name', 'email', 'subject', 'desc')


translator.register(ContactUs, ContactFormTranslationOptions)
