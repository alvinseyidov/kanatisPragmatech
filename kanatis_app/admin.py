from django.contrib import admin

from .models import (
    Post, Carousel, Service, SubService
)


admin.site.register(Post)
admin.site.register(Carousel)
admin.site.register(Service)
admin.site.register(SubService)

