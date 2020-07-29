from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.

class TextPages(models.Model):
    team_member = models.CharField(max_length=255, null=True, blank=True)
    team = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Səhifə yazıları"


class AboutUs(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
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

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = "Komanda"


class TeamServices(models.Model):
    service = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
    serv_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.service}'

    class Meta:
        verbose_name_plural = "Komanda Servisləri"


class SertificateTeam(models.Model):
    sertificate = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
    sertificate_name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Komanda Sertifikati"


class Contact(models.Model):
    address = models.CharField(max_length=255, null=True, blank=True)
    office_hour = models.CharField(max_length=255, null=True, blank=True)
    number = models.CharField(max_length=255, null=True, blank=True)
    text = RichTextField()

    class Meta:
        verbose_name_plural = "Əlaqə"


class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = "Əlaqə Form"
