from matplotlib import pyplot as plt

from visualisation.fits_functions import load_sub_image_data
from visualisation.true_source_functions import get_subset

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


# Load in and open fits file
# TODO: make this file load dynamic, create a model for fits image and a management command to read it in
sub_image = load_sub_image_data(FILENAME, Y_MIN, X_MIN, SIZE)

# Get TrueSource set filtered by pixels limits in sub image
source_set = get_subset(Y_MIN, X_MIN, SIZE)

plot_source_centers_on_image(sub_image, source_set)
plt.show()
