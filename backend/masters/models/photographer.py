from logging import getLogger
from typing import TYPE_CHECKING

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from ya_django_toolkit_jp.base.models import BaseModel

if TYPE_CHECKING:
    from django_stubs_ext.db.models.manager import RelatedManager
    from photos.models import Photo


logger = getLogger(__name__)


class Photographer(BaseModel):
    if TYPE_CHECKING:
        photos: RelatedManager[Photo]

    display_name = models.CharField(
        verbose_name=_("Display name"),
        max_length=255,
        db_index=True,
    )

    real_name = models.CharField(
        verbose_name=_("Real name"),
        max_length=255,
        blank=True,
    )

    copyright = models.CharField(
        verbose_name=_("Copyright"),
        max_length=255,
        blank=True,
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name=_("User"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("Photographer")
        verbose_name_plural = _("Photographers")

    def __str__(self):
        return self.display_name
