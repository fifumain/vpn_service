from core_apps.proxy.models import Site
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import CustomUserChangeForm, UserCreationForm


@login_required
def dashboard(request):

    sites = Site.objects.filter(user=request.user)
    return render(request, "users/dashboard.html", {"sites": sites})


@login_required
def edit_profile(request):

    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = CustomUserChangeForm(instance=request.user)

    return render(request, "users/edit_profile.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # automatically login after successful registration
            return redirect("dashboard")
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})
