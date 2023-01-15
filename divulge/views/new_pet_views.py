from django.http import HttpResponse
from django.shortcuts import render, redirect

from divulge.models.divulge_models import Pet, Tag, Breed


def new_pet_view(request):
    message = None
    if request.method == "GET":
        tags = Tag.objects.all()
        breeds = Breed.objects.all()
        context = {"tags": tags, "breeds": breeds}
        return render(request, "divulge/new_pet.html", context=context)
    elif request.method == "POST":
        picture = request.FILES.get("picture")
        name = request.POST.get("name")
        description = request.POST.get("description")
        province = request.POST.get("province")
        city = request.POST.get("city")
        phone = request.POST.get("phone")
        tags = request.POST.getlist("tags")
        breed = request.POST.get("breed")
        pet = Pet(
            user=request.user,
            picture=picture,
            name=name,
            description=description,
            province=province,
            city=city,
            phone=phone,
            breed_id=breed,
        )
        pet.save()

        for tag_id in tags:
            tag = Tag.objects.get(id=tag_id)
            pet.tags.add(tag)
        pet.save()

        tags = Tag.objects.all()
        breeds = Breed.objects.all()

        message = {"type": "success", "text": "Pet cadastrado com sucesso"}

        context = {"message": message, "tags": tags, "breeds": breeds}

        return render(request, "divulge/new_pet.html", context=context)
