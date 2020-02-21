"""Models to describe the data from the truth catalogue and the generated training data set."""

from django.db import models


class TrueSource(models.model):
    """Model to describe sources contained within a truth catalogue.
     These are the sources we believe we know characteristics of."""

    source_id = models.FloatField()
    ra_core = models.CharField()
    dec_core = models.CharField()
    ra_centroid = models.CharField()
    dec_centroid = models.CharField()
    flux = models.FloatField()
    core_fraction = models.FloatField()

    # bmaj and bmin are in units of arcseconds
    bmaj = models.FloatField()
    bmin = models.FloatField()

    # postition_angle is in units of degrees
    # measured clockwise for the longitute-wise direction
    position_angle = models.FloatField()
    size = models.FloatField()
    classification = models.CharField()
    selection = models.Boolean()

    # cooridnates of the centroid
    x_centroid = models.FloatField()
    y_centroid = models.FloatField()
