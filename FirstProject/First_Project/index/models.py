from django.db import models


# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=700, blank=False)
    image = models.ImageField(upload_to='about/', null=True)

    # for change object name

    def __str__(self):
        return self.title


class Contact(models.Model):
    phone = models.IntegerField(blank=False, null=False)
    address = models.CharField(blank=False, null=False, max_length=100)
    email = models.EmailField(blank=False, null=False)
    telegram = models.URLField(max_length=100, null=True)
    whatsapp = models.URLField(max_length=100, null=True)

    # for change object name
    def __str__(self):
        return self.email


class Contact_form(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=150, blank=False, null=True)
    suggestion = models.TextField(max_length=700, blank=False)

    # for change object name
    def __str__(self):
        return self.full_name
