from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from divulge.models.adoption_application_models import AdoptionApplication
from django.contrib.messages import constants
from django.core.mail import send_mail
from django.contrib import messages
from divulge.models.divulge_models import Pet, Tag, Breed
from django.views.decorators.csrf import csrf_exempt


def see_pets(request, id):
    if request.method == "GET":
        pet = Pet.objects.get(id=id)
        context = {"pet": pet}
        return render(request, "divulge/see_pet.html", context=context)


def adoption_view(request, id_pet):
    pet = Pet.objects.filter(id=id_pet).filter(status="P")
    if not pet.exists():
        messages.add_message(request, constants.WARNING, "Este pet já foi adotado!")
        return redirect("/")
    order = AdoptionApplication(pet=pet.first(), user=request.user, data=datetime.now())
    order.save()
    messages.add_message(
        request, constants.SUCCESS, "Pedido de adoção realizada com sucesso"
    )
    return redirect("/")


def see_orders(request):
    if request.method == "GET":
        orders = AdoptionApplication.objects.filter(user=request.user).filter(
            status="AG"
        )
        return render(request, "divulge/see_orders.html", {"orders": orders})


def process_orders(request, id_order):
    status = request.GET.get("status")
    order = AdoptionApplication.objects.get(id=id_order)
    if status == "A":
        order.status = "AP"
        text = """Olá, sua adoção foi aprovada. ..."""
    elif status == "R":
        text = """Olá, sua adoção foi recusada. ..."""
        order.status = "R"

    order.save()
    email = send_mail(
        "Sua adoção foi processada",
        text,
        "corteisjunior@gmail.com",
        [
            order.user.email,
        ],
    )

    messages.add_message(
        request, constants.SUCCESS, "Pedido de adoção processado com sucesso"
    )
    return redirect("divulge/see_orders")


def dashboard(request):
    if request.method == "GET":
        return render(request, "divulge/dashboard.html")


@csrf_exempt
def adoption_breed_api(request):
    breeds = Breed.objects.all()

    breed_qt = []
    for breed in breeds:
        adoptions = AdoptionApplication.objects.filter(pet__breed=breed).count()
        breed_qt.append(adoptions)

    breeds = [breed.breed for breed in breeds]
    data = {"breed_qt": breed_qt, "labels": breeds}

    return JsonResponse(data)
