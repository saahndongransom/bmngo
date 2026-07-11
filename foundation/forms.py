from django import forms

from .models import Inquiry


class ContactForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ["full_name", "email", "phone", "message"]
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder": "Your name"}),
            "email": forms.EmailInput(attrs={"placeholder": "you@email.com"}),
            "phone": forms.TextInput(attrs={"placeholder": "+237"}),
            "message": forms.Textarea(attrs={"placeholder": "How can we help?", "rows": 5}),
        }


class VolunteerForm(forms.ModelForm):
    availability = forms.ChoiceField(
        choices=[
            ("weekdays", "Weekdays"),
            ("weekends", "Weekends"),
            ("evenings", "Evenings"),
            ("flexible", "Flexible"),
        ],
        widget=forms.Select,
    )
    area_of_interest = forms.ChoiceField(
        choices=[
            ("entrepreneurship", "Youth Entrepreneurship & Economic Empowerment"),
            ("education", "Education, Leadership & Skills Development"),
            ("humanitarian", "Humanitarian Assistance & Community Resilience"),
            ("women", "Women Empowerment & Gender Equality"),
            ("environment", "Environmental Sustainability & Community Well-being"),
        ],
        widget=forms.Select,
    )

    class Meta:
        model = Inquiry
        fields = ["full_name", "email", "phone", "message"]
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder": "Your name"}),
            "email": forms.EmailInput(attrs={"placeholder": "you@email.com"}),
            "phone": forms.TextInput(attrs={"placeholder": "+237"}),
            "message": forms.Textarea(attrs={"placeholder": "Tell us about your skills and why you'd like to volunteer", "rows": 5}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.kind = Inquiry.Kind.VOLUNTEER
        instance.details = {
            "availability": self.cleaned_data["availability"],
            "area_of_interest": self.cleaned_data["area_of_interest"],
        }
        if commit:
            instance.save()
        return instance


class DonateForm(forms.ModelForm):
    GIFT_TYPE = [("one_time", "One-time gift"), ("monthly", "Monthly giving")]
    AMOUNT = [("25000", "25,000 XAF"), ("50000", "50,000 XAF"), ("100000", "100,000 XAF"), ("custom", "Custom amount")]

    gift_type = forms.ChoiceField(choices=GIFT_TYPE, widget=forms.RadioSelect, initial="one_time")
    amount = forms.ChoiceField(choices=AMOUNT, widget=forms.RadioSelect, initial="25000")
    custom_amount = forms.CharField(required=False, widget=forms.TextInput(attrs={"placeholder": "Enter an amount"}))

    class Meta:
        model = Inquiry
        fields = ["full_name", "email", "phone", "message"]
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder": "Your name"}),
            "email": forms.EmailInput(attrs={"placeholder": "you@email.com"}),
            "phone": forms.TextInput(attrs={"placeholder": "+237"}),
            "message": forms.Textarea(attrs={"placeholder": "Anything you'd like us to know? (optional)", "rows": 4}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.kind = Inquiry.Kind.DONATE
        instance.details = {
            "gift_type": self.cleaned_data["gift_type"],
            "amount": self.cleaned_data["custom_amount"] or self.cleaned_data["amount"],
        }
        if commit:
            instance.save()
        return instance


class PartnerForm(forms.ModelForm):
    organization = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Organization name"}))
    partnership_type = forms.ChoiceField(
        choices=[
            ("funding", "Funding / Sponsorship"),
            ("technical", "Technical Assistance"),
            ("csr", "Corporate Social Responsibility"),
            ("research", "Research & Academic Collaboration"),
            ("other", "Other"),
        ],
        widget=forms.Select,
    )

    class Meta:
        model = Inquiry
        fields = ["full_name", "email", "phone", "message"]
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder": "Your name"}),
            "email": forms.EmailInput(attrs={"placeholder": "you@email.com"}),
            "phone": forms.TextInput(attrs={"placeholder": "+237"}),
            "message": forms.Textarea(attrs={"placeholder": "Tell us about your organization and what you have in mind", "rows": 5}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.kind = Inquiry.Kind.PARTNER
        instance.details = {
            "organization": self.cleaned_data["organization"],
            "partnership_type": self.cleaned_data["partnership_type"],
        }
        if commit:
            instance.save()
        return instance
