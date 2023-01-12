from django.db import models
from divulge.models import *
from django.contrib.auth.models import User


class Breed(models.Model):
    """Breed of pets
    Keyword arguments:
    argument -- models
    Return: Breed of pets
    """

    breed = models.CharField(max_length=50)

    def __str__(self):
        return self.breed


class Tag(models.Model):
    """Tag

    Args:
        models Tag: Table

    Returns:
        str: tag
    """

    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag


class Pet(models.Model):
    choices_status = (("P", "Para adocão"), ("A", "Adotado"))

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    picture = models.ImageField(upload_to="fotos_pets")
    name = models.CharField(max_length=50)
    description = models.TextField()
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    phone = PhoneNumberField(region="MZ")
    tags = models.ManyToManyField(Tag)
    breed = models.ForeignKey(Breed, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=1, choices=choices_status, default="p")

    def __str__(self):
        return self.name
