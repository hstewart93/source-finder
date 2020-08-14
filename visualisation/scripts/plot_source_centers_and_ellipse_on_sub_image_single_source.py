"""Plots the subimage given by X_MIN and Y_MIN and plots the true source label as
an ellipse and source center for a single source given by pk of TrueSource object."""

from django.conf import settings
import math
from matplotlib import pyplot as plt
from matplotlib.patches import Ellipse, Rectangle
import numpy as np

from app.fits_functions import load_sub_image_data
from app.true_source_functions import convert_arcseconds_to_pix
from app.true_source_functions import get_subset
from sources.models import TrueSource

# Constants
FILENAME = "/Users/bi19158/Code/ska-challenge-1/SKAMid_B1_8h_v3.fits"
Y_MIN = 17_000
X_MIN = 16_500
SIZE = 500

# Load a subset of the data and truth labels using the x and y pixel limits
data_subset = load_sub_image_data(FILENAME, Y_MIN, X_MIN, SIZE)
label_subset = get_subset(Y_MIN, X_MIN, SIZE)
source_object = TrueSource.objects.get(pk=1445)

source_center_x = source_object.x_centroid - X_MIN
source_center_y = source_object.y_centroid - Y_MIN

# Convert bmaj from arcseconds to pixels
source_object_bmaj = convert_arcseconds_to_pix(source_object.bmaj)

# Convert to position angle to radians for numpy trig functions
source_object_pa = math.radians(source_object.position_angle)

# For TrueSource object pk=1445, the x length of the rectangle is bmaj*cos(pa)
# the y length is bmaj*sin(180-pa)
x_length = source_object_bmaj * np.cos(source_object_pa)
y_length = source_object_bmaj * 2 * np.sin(source_object_pa)

lower_left_x = source_center_x - x_length / 2
lower_left_y = source_center_y - y_length / 2
fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(data_subset, origin="lower")


ellipse = Ellipse(
    xy=(source_center_x, source_center_y),
    width=source_object.bmin / settings.PIX_TO_ARCSECONDS,
    height=source_object.bmaj / settings.PIX_TO_ARCSECONDS,
    angle=-source_object.position_angle + 90,
    fill=False,
    edgecolor="cyan",
    alpha=0.5,
)
rectangle = Rectangle(
    xy=(lower_left_x, lower_left_y),
    width=x_length,
    height=y_length,
    fill=False,
    edgecolor="black",
    alpha=0.5,
)
ax.add_patch(ellipse)
ax.add_patch(rectangle)
ax.scatter(source_center_x, source_center_y, marker="x")

plt.show()
