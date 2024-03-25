from logging import getLogger
from typing import TYPE_CHECKING

from django.contrib.gis.db import models
from django.core import validators
from django.utils.regex_helper import _lazy_re_compile
from django.utils.translation import gettext_lazy as _
from ya_django_toolkit_jp.base.models import BaseModel
from ya_django_toolkit_jp.fields import NormalizeCharField

if TYPE_CHECKING:
    from django_stubs_ext.db.models.manager import ManyRelatedManager
    from photos.models import Photo


logger = getLogger(__name__)


class Tag(BaseModel):
    if TYPE_CHECKING:
        photos: ManyRelatedManager[Photo]

    # タグ名
    name = models.CharField(
        verbose_name=_("Tag name"),
        max_length=255,
        unique=True,
    )

    # 検索用タグ名
    search_name = NormalizeCharField(
        verbose_name=_("Search tag name"),
        editable=False,
        max_length=255,
        db_index=True,
    )

    # タグの説明
    description = models.TextField(
        verbose_name=_("Description"),
        blank=True,
    )

    # 場所
    location = models.CharField(
        verbose_name=_("Location"),
        max_length=255,
        blank=True,
    )

    # 経度
    lon = models.FloatField(
        verbose_name=_("Longitude"),
        blank=True,
        null=True,
    )

    # 緯度
    lat = models.FloatField(
        verbose_name=_("Latitude"),
        blank=True,
        null=True,
    )

    # 緯度経度
    latlng = models.PointField(
        geography=True,
        editable=False,
        null=True,
    )

    # 緯度経度
    latlng_geom = models.PointField(
        editable=False,
        null=True,
    )

    # Google Map Place ID
    google_maps_place_id = models.CharField(
        verbose_name=_("Google Map Place ID"),
        max_length=255,
        validators=[
            validators.RegexValidator(_lazy_re_compile(r"^[!-~]*\Z")),
        ],
        blank=True,
    )
