from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model



User = get_user_model()

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
    content = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
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
    service = models.ForeignKey('Service', on_delete = models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{ self.service.name }'


class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='services/', null=True, blank=True)
    fa_class = models.CharField(max_length = 50)
    
    def __str__(self):
        return f'{ self.name }'


class SubService(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='subservices/')
    content = models.TextField()
    fa_icon = models.CharField(max_length=50)
    service = models.ForeignKey('Service', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

