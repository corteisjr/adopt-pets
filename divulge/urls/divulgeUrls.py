from django.urls import path
from divulge.views.new_pet_views import *
from divulge.views.see_pet_views import *

urlpatterns = [
    path("new_pet", new_pet_view, name="new_pet"),
    path("my_pets", my_pets_view, name="my_pets"),
    path("delete_pet<int:id>", delete_pets, name="delete_pet"),
    path("see_pets/<int:id>", see_pets, name="see_pets"),
    path("adoption/<int:id_pet>", adoption_view, name="adoption"),
    path("see_orders/", see_orders, name="see_orders"),
]
