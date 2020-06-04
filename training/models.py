import numpy as np

from django.db import models
from django.conf import settings


class TrueSource(models.Model):
    """Model to describe sources contained within a truth catalogue.
     These are the sources we believe we know characteristics of."""

    source_id = models.FloatField()
    ra_core = models.CharField(max_length=255)
    dec_core = models.CharField(max_length=255)
    ra_centroid = models.CharField(max_length=255)
    dec_centroid = models.CharField(max_length=255)
    flux = models.FloatField()
    core_fraction = models.FloatField()

    # bmaj and bmin are in units of arcseconds
    bmaj = models.FloatField()
    bmin = models.FloatField()

    # position_angle is in units of degrees
    # measured clockwise for the longitute-wise direction
    position_angle = models.FloatField()
    size = models.FloatField()
    classification = models.CharField(max_length=255)
    selection = models.BooleanField()

    # cooridnates of the centroid
    x_centroid = models.FloatField()
    y_centroid = models.FloatField()

    surface_brightness = models.FloatField(null=True, blank=True)

    def calculate_surface_brightness(self):
        """Method to calculate surface brightness of a source."""
        if not self.bmaj == 0 or not self.bmin == 0:
            ellipse_area = np.pi * self.bmaj * self.bmin
            return self.flux * settings.PIX_TO_ARCSECONDS / ellipse_area

    def save(self, *args, **kwargs):
        """Override the save method to auto-populate the surface brightness field."""
        if not self.surface_brightness:
            self.surface_brightness = self.calculate_surface_brightness()
        super(TrueSource, self).save(*args, **kwargs)
