from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import LeadForm
from .models import Lead
from django.template.loader import get_template


def dashboard(request):
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Lead added successfully.")
            return redirect("dashboard")
        else:
            messages.error(request, "Please fix the errors below and try again.")
    else:
        form = LeadForm()

    leads = Lead.objects.all()

    total_leads = leads.count()
    status_counts = {
        "New": leads.filter(status=Lead.STATUS_NEW).count(),
        "In Progress": leads.filter(status=Lead.STATUS_IN_PROGRESS).count(),
        "Converted": leads.filter(status=Lead.STATUS_CONVERTED).count(),
    }

    context = {
        "form": form,
        "leads": leads,
        "total_leads": total_leads,
        "converted_leads": status_counts["Converted"],
        "new_leads": status_counts["New"],
        "in_progress_leads": status_counts["In Progress"],
        "status_counts": status_counts,
    }
    return render(request, "leads/dashboard.html", context)
