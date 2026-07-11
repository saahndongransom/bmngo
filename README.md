# BM Seed of Hope Foundation — Django Website

A multi-page Django site for BM Seed of Hope Foundation. Every nav item (About,
Programmes, Impact, Partners, Get Involved, Contact) is its own page/URL, plus
dedicated pages for Donate, Volunteer, and Partner inquiries.

## Pages & URLs

| Page | URL |
|---|---|
| Home | `/` |
| About | `/about/` |
| Programmes (5 strategic pillars) | `/programmes/` |
| Impact (theory of change + 5-step model) | `/impact/` |
| Partners | `/partners/` |
| Get Involved (overview) | `/get-involved/` |
| Donate | `/donate/` |
| Volunteer | `/volunteer/` |
| Partner With Us | `/partner/` |
| Contact | `/contact/` |
| Admin | `/admin/` |

## Quick start

```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser  # to log into /admin/
python manage.py runserver
```

Visit http://127.0.0.1:8000/

## How the forms work

Donate, Volunteer, Partner, and Contact each have their own page and their own
`django.forms.ModelForm`, but they all save into a single `Inquiry` model
(`foundation/models.py`) with a `kind` field ("donate", "volunteer", "partner",
"contact") and a `details` JSON field for page-specific fields (e.g. gift
amount, availability). Every submission shows up in Django admin at
`/admin/foundation/inquiry/`, filterable by kind, with a `handled` checkbox
your team can tick once someone follows up.

**Donate is interest-capture only** — it records what a donor wants to give,
it does **not** process payment. To accept real gifts, connect a payment
processor (Stripe, PayPal, or a local mobile money gateway) in
`foundation/views.py::donate`.

## Before you deploy

1. **Set real contact details.** `/contact/` currently shows placeholder text
   (`[add your email address]`, etc.) in `foundation/templates/foundation/contact.html`.
2. **Set `DEBUG = False`** and a real `ALLOWED_HOSTS` list in
   `bmsohf_site/settings.py` (currently `['*']` for local development only).
3. **Set a real `SECRET_KEY`** via an environment variable, not the one
   committed here.
4. **Configure email.** `EMAIL_BACKEND` is currently the console backend (form
   submissions are only saved to the database, not emailed). Point it at a
   real SMTP provider and notify `FOUNDATION_INBOX` in `settings.py` when a
   submission comes in, if you want email alerts too.
5. **Switch the database** from SQLite to Postgres for production, and run
   `python manage.py collectstatic` behind a real web server (nginx/Apache) or
   a static host — Django's dev server should never be used in production.

## Project layout

```
bmsohf_site/
  bmsohf_site/        # project settings, root urls.py
  foundation/          # the one app: models, forms, views, templates, static
    templates/foundation/   # base.html + one template per page
    static/foundation/      # shared CSS + JS (design tokens match the brand palette)
    models.py            # Inquiry model (used by all 4 forms)
    forms.py             # ContactForm, VolunteerForm, DonateForm, PartnerForm
    views.py
    urls.py
    admin.py
  manage.py
  requirements.txt
```
