from django.contrib import admin
from .models import Breed, Tag, Pet, AdoptionApplication

admin.site.register(Breed)
admin.site.register(Tag)
admin.site.register(Pet)
admin.site.register(AdoptionApplication)
