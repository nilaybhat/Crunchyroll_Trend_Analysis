from django.shortcuts import render
from .forms import ContactForm
from .models import ContactMessage


def home(request):
    return render(request, "home.html")


def dashboard(request):
    return render(request, "analysis.html")


def prediction(request):
    return render(request, "prediction.html")


def team(request):
    return render(request, "team.html")


def contact(request):
    form = ContactForm()
    submitted = False

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            ContactMessage.objects.create(**form.cleaned_data)
            submitted = True
            form = ContactForm()

    return render(
        request,
        "contact.html",
        {
            "form": form,
            "submitted": submitted,
        },
    )