from django import forms
from .models import Lead


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ["full_name", "email", "source", "status"]
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder": "e.g. Jane Cooper", "class": "form-control"}),
            "email": forms.EmailInput(attrs={"placeholder": "e.g. jane@company.com", "class": "form-control"}),
            "source": forms.Select(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-control"}),
        }

    def clean_full_name(self):
        full_name = self.cleaned_data.get("full_name", "").strip()
        if not full_name:
            raise forms.ValidationError("Full name is required.")
        return full_name

    def clean_email(self):
        email = self.cleaned_data.get("email", "").strip().lower()

        query = Lead.objects.filter(email__iexact=email)
        if self.instance and self.instance.pk:
            query = query.exclude(pk=self.instance.pk)

        if query.exists():
            raise forms.ValidationError(
                "A lead with this email already exists. Please use a different email."
            )
        return email