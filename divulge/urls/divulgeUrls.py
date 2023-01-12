from django.urls import path
from divulge.views.new_pet_views import *

urlpatterns = [path("new_pet", new_pet_view, name="new_pet")]
