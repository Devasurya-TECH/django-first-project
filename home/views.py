from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def booking(request):
    return render(request, "booking.html")


def doctors(request):
    return render(request, "doctors.html")


def contact(request):
    return render(request, "contact.html")


def services(request):
    return render(request, "services.html")
