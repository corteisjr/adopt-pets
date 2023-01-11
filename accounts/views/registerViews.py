from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from accounts.forms.AuthForm import RegisterForm


@csrf_exempt
def register(request):
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
                return render(request, "accounts/register.html")
            elif verify_email is not None:
                message = {
                    "type": "danger",
                    "text": "Já existe um usuário com este email",
                }
                return render(request, "accounts/register.html")
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
                        message = {
                            "type": "success",
                            "text": "Conta criada com sucesso",
                        }
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
