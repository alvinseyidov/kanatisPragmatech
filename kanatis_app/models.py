from ckeditor.fields import RichTextField
from django.db import models
from django.utils.text import slugify

def latin_slugify(str):
    str = str.replace(" ", "-")
    str = str.replace("?", "-")
    str = str.replace(",", "-")
    str = str.replace("ə", "e")
    str = str.replace("ö", "o")
    str = str.replace("ç", "ch")
    str = str.replace("ş", "sh")
    str = str.replace("ı", "i")
    str = str.replace("ü", "u")
    str = str.replace("ğ", "gh")
    str = str.replace("İ", "i")
    str = str.replace("Ə", "e")
    str = str.replace("Ö", "o")
    str = str.replace("Ü", "u")
    return str.lower()

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    image = models.ImageField(upload_to='postimages/')
    category = models.ForeignKey('Service', related_name='posts', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, null=True, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def save(self, *args, **kwargs):
        self.slug = latin_slugify(self.title[:48])
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'


class Carousel(models.Model):
    content = models.CharField(max_length=100,)
    image = models.ImageField(upload_to = 'carousels/')
    service = models.ForeignKey('Service', related_name='carousels', on_delete = models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{ self.service.name }'


class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='services/', null=True, blank=True)
    fa_class = models.CharField(max_length = 50)
    slug = models.SlugField(unique=True, null=True, editable=False)
    
    def __str__(self):
        return f'{ self.name }'

    def save(self, *args, **kwargs):
        self.slug = latin_slugify(self.name[:48])
        super(Service, self).save(*args, **kwargs)


class SubService(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='subservices/')
    content = RichTextField()
    fa_icon = models.CharField(max_length=50)
    service = models.ForeignKey('Service', related_name='subservice', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, null=True, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        self.slug = latin_slugify(self.title[:48])
        super(SubService, self).save(*args, **kwargs)


class TextPages(models.Model):
    team_member = models.CharField(max_length=255, null=True, blank=True)
    team = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Səhifə yazıları"


class AboutUs(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    img = models.ImageField(upload_to='about/')
    description = RichTextField()

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = "Haqqımızda"


class Team(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    desc = RichTextField()
    status = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    number = models.CharField(max_length=255, null=True, blank=True)
    img = models.ImageField(upload_to='teams')
    facebook = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, editable=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = "Komanda"

    def save(self, *args, **kwargs):
        self.slug = latin_slugify(self.name[:48])
        super(Team, self).save(*args, **kwargs)


class TeamServices(models.Model):
    service = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
    serv_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.service}'

    class Meta:
        verbose_name_plural = "Komanda Servisləri"

    def __str__(self):
        return self.service.name

class SertificateTeam(models.Model):
    sertificate = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
    sertificate_name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Komanda Sertifikati"

    def __str__(self):
        return self.sertificate_name

class Contact(models.Model):
    address = models.CharField(max_length=255, null=True, blank=True)
    gmap_embed_address = models.CharField('Gmap embeded iframe', max_length=1000)
    email = models.EmailField()
    office_hour = models.CharField(max_length=255, null=True, blank=True)
    number = models.CharField(max_length=255, null=True, blank=True)
    text = RichTextField()

    class Meta:
        verbose_name_plural = "Əlaqə"

    def __str__(self):
        return f'{self.email} | {self.address}'

class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = "Əlaqə Form"

class Logo(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='logos/')

    def __str__(self):
        return f'{self.name}'
