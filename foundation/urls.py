from django.urls import path

from . import views

app_name = "foundation"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("programmes/", views.programmes, name="programmes"),
    path("impact/", views.impact, name="impact"),
    path("partners/", views.partners, name="partners"),
    path("get-involved/", views.get_involved, name="get_involved"),
    path("donate/", views.donate, name="donate"),
    path("volunteer/", views.volunteer, name="volunteer"),
    path("partner/", views.partner, name="partner"),
    path("contact/", views.contact, name="contact"),
]
