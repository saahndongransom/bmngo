from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContactForm, DonateForm, PartnerForm, VolunteerForm
from .models import Partner


def home(request):
    return render(request, "foundation/home.html")


def about(request):
    return render(request, "foundation/about.html")


def programmes(request):
    return render(request, "foundation/programmes.html")


def impact(request):
    return render(request, "foundation/impact.html")


def partners(request):
    return render(request, "foundation/partners.html", {"partners": Partner.objects.all()})


def get_involved(request):
    return render(request, "foundation/get_involved.html")


def donate(request):
    if request.method == "POST":
        form = DonateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you — your donation interest has been received. We'll be in touch shortly.")
            return redirect("foundation:donate")
    else:
        form = DonateForm()
    return render(request, "foundation/donate.html", {"form": form})


def volunteer(request):
    if request.method == "POST":
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for applying to volunteer — our team will reach out soon.")
            return redirect("foundation:volunteer")
    else:
        form = VolunteerForm()
    return render(request, "foundation/volunteer.html", {"form": form})


def partner(request):
    if request.method == "POST":
        form = PartnerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you — your partnership inquiry has been received.")
            return redirect("foundation:partner")
    else:
        form = PartnerForm()
    return render(request, "foundation/partner.html", {"form": form})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent — thank you for reaching out. We'll respond as soon as we can.")
            return redirect("foundation:contact")
    else:
        form = ContactForm()
    return render(request, "foundation/contact.html", {"form": form})
