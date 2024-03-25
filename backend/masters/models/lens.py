from logging import getLogger
from typing import TYPE_CHECKING

from django.db import models
from django.utils.translation import gettext_lazy as _
from ya_django_toolkit_jp.base.models import BaseModel
from ya_django_toolkit_jp.fields import NormalizeCharField

if TYPE_CHECKING:
    from django_stubs_ext.db.models.manager import RelatedManager
    from photos.models import Photo


logger = getLogger(__name__)


class Lens(BaseModel):
    if TYPE_CHECKING:
        photos: RelatedManager[Photo]

    # メーカー名
    manufacturer = NormalizeCharField(
        verbose_name=_("Manufacturer name"),
        max_length=255,
        db_index=True,
    )

    # モデル名
    model = NormalizeCharField(
        verbose_name=_("Model name"),
        max_length=255,
        db_index=True,
    )

    # 焦点距離の最小値（mm）
    min_focal_length = models.PositiveIntegerField(
        verbose_name=_("Minimum focal length"),
        blank=True,
        null=True,
    )

    # 焦点距離の最大値（mm）
    max_focal_length = models.PositiveIntegerField(
        verbose_name=_("Maximum focal length"),
        blank=True,
        null=True,
    )

    # 最小絞り値
    min_aperture = models.FloatField(
        verbose_name=_("Minimum aperture"),
        blank=True,
        null=True,
    )

    # 最大絞り値
    max_aperture = models.FloatField(
        verbose_name=_("Maximum aperture"),
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("Lens")
        verbose_name_plural = _("Lenses")

    def __str__(self):
        focal_length = (
            f"{self.min_focal_length}-{self.max_focal_length}mm"
            if self.min_focal_length and self.max_focal_length
            else ""
        )
        aperture = (
            f"f/{self.min_aperture}-{self.max_aperture}"
            if self.min_aperture and self.max_aperture
            else ""
        )

        if focal_length and aperture:
            return f"{self.manufacturer} {self.model} {focal_length} {aperture}"
        elif focal_length:
            return f"{self.manufacturer} {self.model} {focal_length}"
        elif aperture:
            return f"{self.manufacturer} {self.model} {aperture}"
        else:
            return f"{self.manufacturer} {self.model}"
