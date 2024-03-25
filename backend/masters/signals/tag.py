from django.contrib.gis.geos import Point
from django.db.models.signals import pre_save
from django.dispatch import receiver

from ..models import Tag


@receiver(pre_save, sender=Tag)
def tag_model_pre_save_receiver(sender, instance: Tag, *args, **kwargs):
    instance.search_name = instance.name
    instance.latlng = (
        Point(instance.lon, instance.lat) if instance.lon and instance.lat else None
    )
    instance.latlng_geom = (
        Point(instance.lon, instance.lat) if instance.lon and instance.lat else None
    )
