from django.urls import path
from accounts.views.registerViews import *


urlpatterns = [path("register/", register, name="register")]
