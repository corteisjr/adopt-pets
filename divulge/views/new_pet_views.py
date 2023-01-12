from django.shortcuts import render, redirect


def new_pet_view(request):
    if request.method == "GET":
        return render(request, "divulge/new_pet.html")
