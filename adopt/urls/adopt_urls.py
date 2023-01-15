from django.urls import path
from adopt.views.adopt_views import *


urlpatterns = [path("", list_pets, name="list_pets")]
