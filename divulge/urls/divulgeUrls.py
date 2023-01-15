from django.urls import path
from divulge.views.new_pet_views import *

urlpatterns = [
    path("new_pet", new_pet_view, name="new_pet"),
    path("my_pets", my_pets_view, name="my_pets"),
    path("delete_pet<int:id>", delete_pets, name="delete_pet"),
]
