from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout

from accounts.forms.AuthForm import LoginForm, RegisterForm


def login_view(request):
    login_form = LoginForm()
    message = None

    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                _next = request.GET.get("next")
                if _next is not None:
                    return redirect(_next)
                else:
                    return redirect("/")
            else:
                message = {"type": "danger", "text": "Dados do usuário incorrectos"}
                return render(
                    request, "accounts/login.html", context={"message": message}
                )
    message = {
        "type": "success",
        "text": "Conta criada com sucesso",
    }
    context = {"form": login_form, "message": message}

    return render(request, "accounts/login.html", context=context)


@csrf_exempt
def register_view(request):
    """_Register_"""
    register_form = RegisterForm()
    message = None

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            verify_username = User.objects.filter(username=username).first()
            verify_email = User.objects.filter(email=email).first()

            if verify_username is not None:
                message = {
                    "type": "danger",
                    "text": "Já existe um usuário com este nome!",
                }
                return render(
                    request, "accounts/register.html", context={"message": message}
                )
            elif verify_email is not None:
                message = {
                    "type": "danger",
                    "text": "Já existe um usuário com este email",
                }
                return render(
                    request, "accounts/register.html", context={"message": message}
                )
            else:
                if password != confirm_password:
                    message = {
                        "type": "danger",
                        "text": "As senhas não condizem!",
                    }
                    return render(request, "accounts/register.html")
                else:
                    user = User.objects.create_user(username, email, password)
                    if user is not None:
                        return redirect("login")
                    else:
                        message = {
                            "type": "danger",
                            "text": "Um erro ocorreu ao tentar criar a conta.",
                        }

        else:
            message = {
                "type": "danger",
                "text": "Preencha todos os campos!.",
            }
            context = {"message": message}
            return render(request, "accounts/register.html", context=context)
    context = {"form": register_form, "message": message}

    return render(request, "accounts/register.html", context=context)


def logout_view(request):
    logout(request)
    return redirect("/login")
