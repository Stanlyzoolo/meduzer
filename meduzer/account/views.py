from django.http import HttpResponse, request
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.Post)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse("Аутентификация прошла успешно")
            else:
                return HttpResponse("Несуществующая учетная запись")
        else:
            return HttpResponse("Неверное имя пользователя")
    else:
        form = LoginForm()
    return render(request, "account/login.html", {"form": form})


@login_required
def dashboard(request):
    return render(request, "account/dashboard.html", {"section": dashboard})