"""Import FITS image data and generate cut out data for
training based on x and y pixel limits chosen."""

from django.conf import settings
import math
from matplotlib import pyplot as plt
import numpy as np

from app.fits_functions import load_sub_image_data
from app.true_source_functions import convert_arcseconds_to_pix, get_subset
from sources.models import TrueSource

# Constants
FILENAME = "/Users/bi19158/Code/ska-challenge-1/SKAMid_B1_8h_v3.fits"
Y_MIN = 17_000
X_MIN = 16_500
SIZE = 500


# Load a subset of the data and truth labels using the x and y pixel limits
data_subset = load_sub_image_data(FILENAME, Y_MIN, X_MIN, SIZE)
label_subset = get_subset(Y_MIN, X_MIN, SIZE)


def is_even(number):
    """Returns True if the number parsed is even."""
    if number % 2 == 0:
        return True
    else:
        return False


def create_source_cutout(image, y_center, x_center, y_size, x_size):
    """y_size and x_size must be integers"""
    # TODO: add check and raise validation error if not int
    if not is_even(y_size):
        y_size += 1
    if not is_even(x_size):
        x_size += 1
    return image[
        int(y_center - y_size / 2) : int(y_center + y_size / 2),
        int(x_center - x_size / 2) : int(x_center + x_size / 2),
    ]


def get_rounded_source_centers(source, subset_x, subset_y):
    """To slice the image array around the source center the slice indices
    must be integers. Here we use round() first as int() always rounds down
    and since the source size is small this rounding error would offset the
    source cutout too much.

    :parameter subset_x: the minimum x value that was used to create the subset
    :parameter subset_y: the minimum y value that was used to create the subset
    """
    return (
        int(round(source.x_centroid - subset_x)),
        int(round(source.y_centroid - subset_y)),
    )


source_object = TrueSource.objects.get(pk=22060)

source_center_x, source_center_y = get_rounded_source_centers(
    source_object, X_MIN, Y_MIN
)

# Convert bmaj from arcseconds to pixels
source_object_bmaj = convert_arcseconds_to_pix(source_object.bmaj)

# Convert to position angle to radians for numpy trig functions
source_object_pa = math.radians(source_object.position_angle)

# For TrueSource object pk=1445, the x length of the rectangle is bmaj*cos(pa)
# the y length is bmaj*sin(180-pa)
x_length = int(round(source_object_bmaj * np.cos(source_object_pa)))

# TODO: Figure out why this works
# If position angle is less than 45 degrees then bmaj has to be multiplied by two
# Take absolute as some angles are negative
if abs(source_object.position_angle) < 45:
    y_length = int(round(source_object_bmaj * 2 * np.sin(source_object_pa)))
else:
    y_length = int(round(source_object_bmaj * np.sin(source_object_pa)))

# source_cutout = create_source_cutout(data_subset, source_center_y, source_center_x, y_length, x_length)
# plt.imshow(source_cutout, origin="lower")
# plt.show()


# TODO: cut out data around source according to truth (so no extra) - rotate according to position angle - then calulcate
# std of array - set number of stds to go out to in the direction from the source - use this to make cutout


# TODO: something has gone very wrong with the trigonometry and one side is twice as big as it should be!

# To get the ellipse and source center on the cut out image, subtract the lower left values from the center values
# as done when scaling source centers for subset
