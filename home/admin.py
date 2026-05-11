from django.contrib import admin
from django.utils.html import format_html

from .models import Appointment, Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):

    list_display = ("name", "specialty", "image_preview", "is_active", "created_at")

    list_filter = ("is_active", "specialty")

    search_fields = ("name", "specialty")

    fields = ("name", "specialty", "image", "bio", "is_active")

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:48px;height:48px;object-fit:cover;border-radius:8px;" />',
                obj.image.url,
            )
        if obj.image_url:
            return format_html(
                '<img src="{}" style="width:48px;height:48px;object-fit:cover;border-radius:8px;" />',
                obj.image_url,
            )
        return "No image"

    image_preview.short_description = "Photo"


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    list_display = (
        "patient_name",
        "department",
        "appointment_date",
        "appointment_time",
        "created_at",
    )

    search_fields = ("patient_name", "email", "phone", "department")
