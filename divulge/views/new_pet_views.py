from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

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

        pets = Pet.objects.all()
        tags = Tag.objects.all()
        breeds = Breed.objects.all()

        message = {"type": "success", "text": "Pet cadastrado com sucesso"}

        context = {"message": message, "tags": tags, "breeds": breeds, "pets": pets}

        return render(request, "divulge/my_pets.html", context=context)


def my_pets_view(request):
    if request.method == "GET":
        pets = Pet.objects.filter(user=request.user)
        return render(request, "divulge/my_pets.html", {"pets": pets})


def delete_pets(request, id):
    pets = get_object_or_404(Pet, pk=id)
    if not pets.user == request.user:
        messages.info(request, "Este Pet não te pertence")
        return redirect("my_pets")
    pets.delete()
    messages.info(request, "Pet deletado com sucesso!")
    return redirect("my_pets")
