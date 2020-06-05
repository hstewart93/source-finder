"""Models to describe the data from the truth catalogue and the generated training data set."""

from django.db import models


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

    # co-ordinates of the centroid
    x_centroid = models.FloatField()
    y_centroid = models.FloatField()

    # surface brightness field to be populated on save
    surface_brightness = models.FloatField(null=True, blank=True)
