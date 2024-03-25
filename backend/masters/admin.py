from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from . import models


@admin.register(models.Camera)
class CameraAdmin(admin.ModelAdmin):
    list_display = ("manufacturer", "model")
    search_fields = ("manufacturer", "model")
    list_filter = ("manufacturer", "model")
    fieldsets = (
        (
            _("Camera"),
            {
                "fields": (
                    "manufacturer",
                    "model",
                )
            },
        ),
    )
    readonly_fields = ("created_at", "updated_at")


@admin.register(models.Lens)
class LensAdmin(admin.ModelAdmin):
    list_display = ("manufacturer", "model")
    search_fields = ("manufacturer", "model")
    list_filter = ("manufacturer", "model")
    fieldsets = (
        (
            _("Lens"),
            {
                "fields": (
                    "manufacturer",
                    "model",
                )
            },
        ),
        (
            _("Focal length"),
            {
                "fields": (
                    "min_focal_length",
                    "max_focal_length",
                )
            },
        ),
        (
            _("Aperture"),
            {
                "fields": (
                    "min_aperture",
                    "max_aperture",
                )
            },
        ),
    )
    readonly_fields = ("created_at", "updated_at")


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)
    fieldsets = (
        (
            _("Tag"),
            {"fields": ("name",)},
        ),
        (
            _("Description"),
            {"fields": ("description",)},
        ),
        (
            _("Location"),
            {
                "fields": (
                    "location",
                    "lon",
                    "lat",
                )
            },
        ),
        (
            _("Google Map"),
            {"fields": ("google_maps_place_id",)},
        ),
    )
    readonly_fields = ("created_at", "updated_at")
