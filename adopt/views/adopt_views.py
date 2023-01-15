from django.shortcuts import render
from divulge.models.divulge_models import *


def list_pets(request):
    if request.method == "GET":
        pets = Pet.objects.filter(status="P")
        breeds = Breed.objects.all()

        city = request.GET.get("city")
        breeds_filter = request.GET.get("breed")

        if city is not None:
            pets = pets.filter(city__icontains=city)

        if city is not None:
            pets = pets.filter(breed_id=breeds_filter)

        context = {
            "pets": pets,
            "breeds": breeds,
            "city": city,
            "breeds_filter": breeds_filter,
        }
        return render(request, "adopt/list_pets.html", context=context)
