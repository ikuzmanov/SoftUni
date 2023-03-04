from django.shortcuts import render, redirect, get_object_or_404

from car_collection.web.forms import CreateUserProfileForm, CreateCarForm
from car_collection.web.models import Profile, Car


def show_index(request):
    user_profile = Profile.objects.all().first()
    context = {
        "user_profile": user_profile
    }
    return render(request, "index.html", context)


def create_profile(request):
    form = CreateUserProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('show catalogue')

    context = {
        "form": form,
    }
    return render(request, "profile/profile-create.html", context)


def show_catalogue(request):
    user_profile = Profile.objects.all().first()
    cars = Car.objects.all()
    cars_count = Car.objects.all().count()
    context = {
        "user_profile": user_profile,
        "cars": cars,
        "cars_count": cars_count,
    }
    return render(request, "catalogue.html", context)


def create_car(request):
    user_profile = Profile.objects.all().first()
    form = CreateCarForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('show catalogue')

    context = {
        "form": form,
        "user_profile": user_profile,
    }
    return render(request, "car/car-create.html", context)


def details_car(request, id):
    car = get_object_or_404(Car, pk=id)
    user_profile = Profile.objects.all().first()
    context = {
        "car": car,
        "user_profile": user_profile,
    }

    return render(request, "car/car-details.html", context)


def edit_car(request):
    return render(request, "car/car-edit.html")


def delete_car(request):
    return render(request, "car/car-delete.html")


def details_profile(request):
    return render(request, "profile/profile-details.html")


def edit_profile(request):
    return render(request, "profile/profile-edit.html")


def delete_profile(request):
    return render(request, "profile/profile-delete.html")
