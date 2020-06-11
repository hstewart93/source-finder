from django.conf import settings
from matplotlib import pyplot as plt
from matplotlib.patches import Ellipse

from visualisation.fits_functions import (
    clip_image,
    convolve_image,
    create_sub_image,
    read_in_fits,
)
from visualisation.true_source_functions import get_subset, surface_brightness_for_set

# Constants
FILENAME = "/Users/bi19158/Code/ska-challenge-1/SKAMid_B1_8h_v3.fits"
Y_MIN = 17500
X_MIN = 16500
SIZE = 500


def plot_source_centers_on_image(image, query_set):
    """"""
    y_values = [source.y_centroid - Y_MIN for source in query_set]
    x_values = [source.x_centroid - X_MIN for source in source_set]

    plt.scatter(x_values[:100], y_values[:100], marker="x")
    plt.imshow(image)


def plot_ellipse_on_image(image, query_set):
    """"""
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.imshow(image)

    for source in query_set[:100]:
        ellipse = Ellipse(
            xy=(source.x_centroid - X_MIN, source.y_centroid - Y_MIN),
            width=source.bmin / settings.PIX_TO_ARCSECONDS,
            height=source.bmaj / settings.PIX_TO_ARCSECONDS,
            angle=source.position_angle,
            fill=False,
            edgecolor="cyan",
            alpha=0.5,
        )
        ax.add_patch(ellipse)


def plot_convolved_clipped_image(image):
    """"""
    convolved_image = convolve_image(image)
    clipped_image = clip_image(convolved_image, 0)
    plt.imshow(clipped_image)


# Load in and open fits file
# TODO: make this file load dynamic, create a model for fits image and a management command to read it in
image_data = read_in_fits(FILENAME)

sub_image = create_sub_image(image_data, Y_MIN, X_MIN, SIZE)

# Get TrueSource set filtered by pixels limits in sub image
source_set = get_subset(Y_MIN, X_MIN, SIZE)

# Calculate surface brightness for set and order by surface brightness ascending
sorted_set = surface_brightness_for_set(source_set).order_by("-flux")

# plot_source_centers_on_image(sub_image, source_set)
plot_ellipse_on_image(sub_image, sorted_set)
# plot_convolved_clipped_image(sub_image)
plt.show()
