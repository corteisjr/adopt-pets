from django.shortcuts import render, redirect, get_object_or_404
from divulge.models.divulge_models import Pet, Tag, Breed


def see_pets(request, id):
    if request.method == "GET":
        pet = Pet.objects.get(id=id)
        context = {"pet": pet}
        return render(request, "divulge/see_pet.html", context=context)
