from django.db import models


class Lead(models.Model):
    SOURCE_CHOICES = [
        ("LinkedIn", "LinkedIn"),
        ("Website", "Website"),
        ("Referral", "Referral"),
        ("Cold Call", "Cold Call"),
        ("Event", "Event"),
        ("Other", "Other"),
    ]

    STATUS_NEW = "New"
    STATUS_IN_PROGRESS = "In Progress"
    STATUS_CONVERTED = "Converted"

    STATUS_CHOICES = [
        (STATUS_NEW, "New"),
        (STATUS_IN_PROGRESS, "In Progress"),
        (STATUS_CONVERTED, "Converted"),
    ]

    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    source = models.CharField(max_length=50, choices=SOURCE_CHOICES, default="Website")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_NEW)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} <{self.email}> - {self.status}"
