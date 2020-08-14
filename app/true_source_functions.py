from django.conf import settings
import numpy as np

from sources.models import TrueSource


def get_subset(y_min, x_min, size):
    """Get subset of TrueSource catalogue for sub_image pixel limits"""
    return TrueSource.objects.filter(
        y_centroid__gte=y_min,
        y_centroid__lte=y_min + size,
        x_centroid__gte=x_min,
        x_centroid__lte=x_min + size,
    )


def get_sorted_subset(y_min, x_min, size, sort_by):
    """Order subset by given field"""
    source_set = get_subset(y_min, x_min, size)
    return source_set.order_by(sort_by)


def calculate_surface_brightness(source):
    """Method to calculate surface brightness of a source."""
    if not source.bmaj == 0 or not source.bmin == 0:
        ellipse_area = np.pi * source.bmaj * source.bmin
        return source.flux * settings.PIX_TO_ARCSECONDS / ellipse_area


def surface_brightness_for_set(query_set):
    """Batch calculate surface_brightness for a queryset of sources"""
    for source in query_set:
        if not source.surface_brightness:
            source.surface_brightness = calculate_surface_brightness(source)
            source.save()
    return query_set


def convert_arcseconds_to_pix(value, scaling_factor=settings.PIX_TO_ARCSECONDS):
    """Uses PIX_TO_ARCSECONDS from settings.py to convert a measurement
    from arcseconds to pixels."""
    return value / scaling_factor
