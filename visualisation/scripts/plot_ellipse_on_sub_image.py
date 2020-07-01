from django.conf import settings
from matplotlib import pyplot as plt
from matplotlib.patches import Ellipse

from visualisation.fits_functions import load_sub_image_data
from visualisation.true_source_functions import get_sorted_subset

# Constants
FILENAME = "/Users/bi19158/Code/ska-challenge-1/SKAMid_B1_8h_v3.fits"
Y_MIN = 17500
X_MIN = 16500
SIZE = 500


def plot_ellipse_on_image(image, query_set):
    """Plot image with labels from truth catalogue as ellipses"""
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


# Load in and open fits file
# TODO: make this file load dynamic, create a model for fits image and a management command to read it in
sub_image = load_sub_image_data(FILENAME, Y_MIN, X_MIN, SIZE)

# Get TrueSource set filtered by pixels limits in sub image
sorted_set = get_sorted_subset(Y_MIN, X_MIN, SIZE, "-flux")

plot_ellipse_on_image(sub_image, sorted_set)
plt.show()
