from django.urls import path
from accounts.views.registerViews import *


urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
]
