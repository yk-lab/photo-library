from logging import getLogger
from typing import TYPE_CHECKING

from django.utils.translation import gettext_lazy as _
from ya_django_toolkit_jp.base.models import BaseModel
from ya_django_toolkit_jp.fields import NormalizeCharField

if TYPE_CHECKING:
    from django_stubs_ext.db.models.manager import RelatedManager
    from photos.models import Photo


logger = getLogger(__name__)


class Camera(BaseModel):
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

    class Meta:
        verbose_name = _("Camera")
        verbose_name_plural = _("Cameras")

    def __str__(self):
        return f"{self.manufacturer} {self.model}"
