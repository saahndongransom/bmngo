from django.db import models


class Inquiry(models.Model):
    """A single model backs the Contact, Volunteer, Donate, and Partner pages.

    Each page sets `kind` automatically; `details` holds the fields that are
    specific to that page (e.g. availability for volunteers, gift amount for
    donors) so we don't need four near-identical tables.
    """

    class Kind(models.TextChoices):
        CONTACT = "contact", "General inquiry"
        VOLUNTEER = "volunteer", "Volunteer application"
        DONATE = "donate", "Donation interest"
        PARTNER = "partner", "Partnership inquiry"

    kind = models.CharField(max_length=20, choices=Kind.choices, default=Kind.CONTACT)
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    message = models.TextField(blank=True)
    details = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    handled = models.BooleanField(default=False, help_text="Mark as done once someone has followed up.")

    class Meta:
        verbose_name = "Inquiry"
        verbose_name_plural = "Inquiries"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.get_kind_display()} — {self.full_name} ({self.created_at:%Y-%m-%d})"


class SiteSettings(models.Model):
    """Singleton: the small set of details that actually change from time to time —
    contact info and social links. Everything else (mission, pillars, values,
    founder's letter) lives in the templates since it essentially never changes.
    """

    contact_email = models.EmailField(default="info@bmseedofhope.org")
    contact_phone = models.CharField(max_length=40, blank=True)
    address = models.CharField(max_length=240, blank=True)
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)

    class Meta:
        verbose_name = "Site settings"
        verbose_name_plural = "Site settings"

    def __str__(self):
        return "Site settings"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class Partner(models.Model):
    """Organizations the Foundation works with — the one thing on this site
    that genuinely grows over time as new partnerships form."""

    order = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=160)
    logo = models.ImageField(upload_to="partners/", blank=True, null=True)
    website = models.URLField(blank=True)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name
